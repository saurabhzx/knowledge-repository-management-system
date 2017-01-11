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

from .models import Question, QuestionAnalytic, QuestionFollower, QuestionTag
from .serializers import QuestionSerializer, QuestionAnalyticSerializer, QuestionFollowerSerializer, QuestionDetailSerializer, QuestionTagSerializer


"""
This is the API for Question
"""


class QuestionList(generics.ListAPIView):
    """
    List view of questions
    owner -- Owner username
    status -- status 1 or 0
    order_by -- created_on, views
    search   -- full text search
    """
    renderer_classes = (JSONRenderer, )
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    paginate_by = 50

    def get_queryset(self):
        status = self.request.QUERY_PARAMS.get('status', None)
        owner = self.request.QUERY_PARAMS.get('owner', None)
        search = self.request.QUERY_PARAMS.get('search', None)
        order_by = self.request.QUERY_PARAMS.get('order_by', 'created_on')
        if order_by == 'created_on':
            order_by = '-created_on'
        if search:
            return Question.objects.text_search_name(search)
        filters = {}
        if status:
            filters['status'] = status
        if owner:
            filters['owner__username'] = owner

        return Question.objects.filter(**filters).order_by(order_by)

    def post(self, request, *args, **kwargs):
        """
        Create new Question
        """
        user = request.user
        print user
        if(user.is_anonymous()):
            return Response("message:Please logged in to post", status=status.HTTP_401_UNAUTHORIZED)
        self.serializer_class = QuestionSerializer
        data = request.DATA.copy()
        owner = request.user.pk
        print owner
        data['owner'] = owner
        print data
        print "hellooooooooooo"
        serializer = QuestionSerializer(data=data)
        print serializer.data
        if serializer.is_valid():
            serializer.save()
            question = serializer.object
            QuestionAnalytic.objects.create(question=question)
            keywords__name = data.get('tags', None).strip().split(",")
            for name in keywords__name:
                print name
                key_obj, created = QuestionTag.objects.get_or_create(name=name)
                key_obj.questions.add(question)
                print name
                key_obj.save()
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)


"""
API for question detail
"""

class QuestionDetail(generics.RetrieveAPIView):
    renderer_classes = (JSONRenderer, )
    serializer_class = QuestionDetailSerializer
    queryset = Question.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)

    def get_object(self):
		try:
			question__pk = self.kwargs.get('question__pk', None)
			return Question.objects.get(pk=question__pk)
		except:
			raise Http404

    def get_view_owner(self):
		return self.get_object().owner

    def post(self, request, *args, **kwargs):
        """
        Edit question details
        """
        question = self.get_object()
        print "i am here "
        print question
        data = request.DATA.copy()
        data['owner'] = request.user.pk
        print data
        serializer = QuestionDetailSerializer(question, data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        data = serializer.data
        return Response(data)


"""
API for Question Analytics
"""
class QuestionAnalyticDetail(generics.ListAPIView):
    renderer_classes = (JSONRenderer, )
    serializer_class = QuestionAnalyticSerializer
    queryset = QuestionAnalytic.objects.all()
    paginate_by = 50

    def post(self, request, *args, **kwargs):
        """
        Edit question analytics details
        """
        print "hello....."
        question__pk = self.kwargs.get('question__pk', None)
        question_analytics = QuestionAnalytic.objects.get(question__pk=question__pk)
        print question_analytics
        data = request.DATA.copy().get('question_analytic',None)
        data['question'] = question__pk
        print data
        serializer = QuestionAnalyticSerializer(question_analytics, data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        data = serializer.data
        return Response(data)


"""
API for QuestionTag
"""


class QuestionTagList(generics.ListAPIView):

    """
    Get question  keywords
    """
    serializer_class = QuestionTagSerializer
    queryset = QuestionTag.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
    paginate_by = 12

    def get_view_owner(self):
        question__pk = self.kwargs.get('question__pk', None)
        question = Question.objects.get(pk=question__pk)
        return question.owner

    def get_queryset(self):
        question__pk = self.kwargs.get('question__pk', None)
        return QuestionTag.objects.filter(questions__pk=question__pk)

    def post(self, request, *args, **kwargs):
        """
        Edit/post tags
        """
        data = request.DATA
        keywords__name = data.get('tags', None).strip().split(",")
        print keywords__name
        question__pk = self.kwargs.get('question__pk', None)
        print question__pk
        try:
            question = Question.objects.get(pk=question__pk)
            print question
        except:
            raise Http404

        for name in keywords__name:
            print name
            key_obj, created = QuestionTag.objects.get_or_create(name=name)
            key_obj.questions.add(question)
            print name
            key_obj.save()
        serializer = QuestionTagSerializer(self.get_queryset())
        return Response(serializer.data)


"""
API for Question Follower
"""
class QuestionFollowerDetail(generics.RetrieveAPIView):
    renderer_classes = (JSONRenderer, )
    serializer_class = QuestionFollowerSerializer
    queryset = QuestionFollower.objects.all()