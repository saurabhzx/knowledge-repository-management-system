import json

from django.conf import settings
from django.http import Http404

from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework import parsers
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render_to_response
from django.core.exceptions import PermissionDenied

from core.permissions.permissions import IsOwner, ReadOnly, IsOwnerOrReadOnly
from core.questions.models import Question

from .models import Answer
from .serializers import AnswerSerializer, AnswerDetailSerializer


"""
This is the API for Answer
"""


class AnswerList(generics.ListAPIView):
    """
    List view of answers
    owner -- Owner username
    status -- status 1 or 0
    order_by -- created_on, views
    """
    renderer_classes = (JSONRenderer, )
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    paginate_by = 20

    def get_queryset(self):
        question__pk = self.kwargs.get('question__pk', None)
        order_by = self.request.QUERY_PARAMS.get('order_by', 'created_on')
        if order_by == 'created_on':
            order_by = '-created_on'
        filters = {}
        if question__pk:
            filters['question__pk'] = question__pk
        return Answer.objects.filter(**filters).order_by(order_by)

    def post(self, request, *args, **kwargs):
        """
        Create new Question
        """
        user = request.user
        print user
        question__pk = self.kwargs.get('question__pk', None)
        question = Question.objects.get(id=question__pk)
        if(user.is_anonymous()):
            return Response("message:Please logged in to post", status=status.HTTP_401_UNAUTHORIZED)
        self.serializer_class = AnswerSerializer
        data = request.DATA.copy()
        print data
        answer, created = Answer.objects.get_or_create(question=question, user_answer=user, answer=data['answer'])
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)


"""
API for answers detail
"""

class AnswerDetail(generics.RetrieveAPIView):
    renderer_classes = (JSONRenderer, )
    serializer_class = AnswerDetailSerializer
    queryset = Answer.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)

    def get_object(self):
		try:
			question__pk = self.kwargs.get('question__pk', None)
			return Answer.objects.get(question__pk=question__pk)
		except:
			raise Http404

    def get_view_owner(self):
		return self.get_object().user_answer

    def post(self, request, *args, **kwargs):
        """
        Edit answer details
        """
        answer = self.get_object()
        print "i am here "
        print answer
        data = request.DATA.copy()
        data['user_answer'] = request.user.pk
        print data
        serializer = AnswerDetailSerializer(answer, data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        data = serializer.data
        return Response(data)