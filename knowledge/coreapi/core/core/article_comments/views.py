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
from core.articles.models import Article

from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


"""
This is the API for Comment
"""


class CommentList(generics.ListAPIView):
    """
    List view of Comment
    owner -- Owner username
    status -- status 1 or 0
    order_by -- created_on, views
    """
    renderer_classes = (JSONRenderer, )
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    paginate_by = 20

    def get_queryset(self):
        article__pk = self.kwargs.get('article__pk', None)
        order_by = self.request.QUERY_PARAMS.get('order_by', 'created_on')
        if order_by == 'created_on':
            order_by = '-created_on'
        filters = {}
        if article__pk:
            filters['article__pk'] = article__pk
        return Comment.objects.filter(**filters).order_by(order_by)

    def post(self, request, *args, **kwargs):
        """
        Create new Comment
        """
        user = request.user
        print user
        article__pk = self.kwargs.get('article__pk', None)
        article = Article.objects.get(id=article__pk)
        if(user.is_anonymous()):
            return Response("message:Please logged in to post", status=status.HTTP_401_UNAUTHORIZED)
        self.serializer_class = CommentSerializer
        data = request.DATA.copy()
        print data
        comment, created = Comment.objects.get_or_create(article=article, user_comment=user, comment=data['comment'])
        serializer = CommentSerializer(comment)
        return Response(serializer.data)


"""
API for Comment detail
"""

class CommentDetail(generics.RetrieveAPIView):
    renderer_classes = (JSONRenderer, )
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)

    def get_object(self):
		try:
			article__pk = self.kwargs.get('article__pk', None)
			return Comment.objects.get(article__pk=article__pk)
		except:
			raise Http404

    def get_view_owner(self):
		return self.get_object().user_comment

    def post(self, request, *args, **kwargs):
        """
        Edit comment details
        """
        comment = self.get_object()
        print "i am here "
        print comment
        data = request.DATA.copy()
        data['user_comment'] = request.user.pk
        print data
        serializer = CommentDetailSerializer(comment, data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        data = serializer.data
        return Response(data)