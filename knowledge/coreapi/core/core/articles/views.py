import json

from django.conf import settings
from django.http import Http404

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render_to_response
from django.core.exceptions import PermissionDenied

from core.permissions.permissions import IsOwner, ReadOnly, IsOwnerOrReadOnly

from .models import Article, ArticleAnalytic, ArticleTag
from .serializers import ArticleSerializer, ArticleDetailSerializer, ArticleAnalyticSerializer, ArticleTagSerializer


"""
This is the API for Article
"""


class ArticleList(generics.ListAPIView):
    """
    List view of articles
    owner -- Owner username
    status -- status 1 or 0
    order_by -- created_on, views
    search -- full text search
    """
    renderer_classes = (JSONRenderer, )
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    paginate_by = 50

    def get_queryset(self):
        status = self.request.QUERY_PARAMS.get('status', None)
        owner = self.request.QUERY_PARAMS.get('owner', None)
        search = self.request.QUERY_PARAMS.get('search', None)
        order_by = self.request.QUERY_PARAMS.get('order_by', 'created_on')
        if order_by == 'created_on':
            order_by = '-created_on'
        if search:
            return Article.objects.text_search_name(search)
        filters = {}
        if status:
            filters['status'] = status
        if owner:
            filters['owner__username'] = owner

        return Article.objects.filter(**filters).order_by(order_by)

    def post(self, request, *args, **kwargs):
        """
        Create new Question
        """
        user = request.user
        print user
        if(user.is_anonymous()):
            return Response("message:Please logged in to post", status=status.HTTP_401_UNAUTHORIZED)
        self.serializer_class = ArticleSerializer
        data = request.DATA.copy()
        print data
        print request.FILES;
        owner = request.user.pk
        data['owner'] = owner
        data['file'] = request.FILES.get('file', None)
        print data['tags']
        print data
        article = Article.objects.create(owner=request.user,title=data['title'],
                                            description=data['description'],file=data['file'])
        article.save();
        ArticleAnalytic.objects.create(article=article)

        keywords__name = data.get('tags', None).strip().split(",")
        for name in keywords__name:
            print name
            key_obj, created = ArticleTag.objects.get_or_create(name=name)
            key_obj.articles.add(article)
            print name
            key_obj.save()
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


"""
API for Article detail
"""

class ArticleDetail(generics.RetrieveAPIView):
    renderer_classes = (JSONRenderer, )
    serializer_class = ArticleDetailSerializer
    queryset = Article.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)

    def get_object(self):
        try:
            article__pk = self.kwargs.get('article__pk', None)
            return Article.objects.get(pk=article__pk)
        except:
            raise Http404

    def get_view_owner(self):
        return self.get_object().owner

    def post(self, request, *args, **kwargs):
        """
        Edit question details
        """
        article = self.get_object()
        print "i am here "
        print article
        data = request.DATA.copy()
        print data
        data['owner'] = request.user.pk
        data['file'] = request.FILES.get('file', None)
        article.file = data['file']
        article.title = data['title']
        article.description = data['description']
        article.save()
        print data
        print "Helllllooooooooooooooooooooooo"
        serializer = ArticleDetailSerializer(article)
        data = serializer.data
        return Response(data)


"""
API for Article Analytics
"""
class ArticleAnalyticDetail(generics.ListAPIView):
    renderer_classes = (JSONRenderer, )
    serializer_class = ArticleAnalyticSerializer
    queryset = ArticleAnalytic.objects.all()
    paginate_by = 50

    def post(self, request, *args, **kwargs):
        """
        Edit question analytics details
        """
        print "hello....."
        article__pk = self.kwargs.get('article__pk', None)
        article_analytics = ArticleAnalytic.objects.get(article__pk=article__pk)
        print article_analytics
        data = request.DATA.copy().get('article_analytic',None)
        data['article'] = article__pk
        print data
        serializer = ArticleAnalyticSerializer(article_analytics, data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        data = serializer.data
        return Response(data)


"""
API for Article Tags
"""


class ArticleTagList(generics.ListAPIView):

    """
    Get brand profile keywords
    """
    serializer_class = ArticleTagSerializer
    queryset = ArticleTag.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
    paginate_by = 12

    def get_view_owner(self):
        article__pk = self.kwargs.get('article__pk', None)
        article = Article.objects.get(pk=article__pk)
        return article.owner

    def get_queryset(self):
        article__pk = self.kwargs.get('article__pk', None)
        return ArticleTag.objects.filter(articles__pk=article__pk)

    def post(self, request, *args, **kwargs):
        """
        Edit/post tags
        """
        data = request.DATA
        keywords__name = json.loads(data.get('tags', None))
        print keywords__name
        article__pk = self.kwargs.get('article__pk', None)
        print article__pk
        try:
            article = Article.objects.get(pk=article__pk)
            print article
        except:
            raise Http404

        for name in keywords__name:
            print name
            key_obj, created = ArticleTag.objects.get_or_create(name=name)
            key_obj.articles.add(article)
            print name
            key_obj.save()
        serializer = ArticleTagSerializer(self.get_queryset())
        return Response(serializer.data)
