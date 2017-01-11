from django.conf.urls import *

from .views import ArticleList, ArticleDetail, ArticleAnalyticDetail, ArticleTagList

urlpatterns = patterns(
    '',
    url(r'^$', ArticleList.as_view(), name='article-list'),
    url(r'^/(?P<article__pk>[0-9]+)$',
        ArticleDetail.as_view(), name='article-detail'),
    url(r'^/(?P<article__pk>[0-9]+)/analytics$',
        ArticleAnalyticDetail.as_view(), name='analytics-article'),
	url(r'^/(?P<article__pk>[0-9]+)/tags$', ArticleTagList.as_view(), name='tag-list'),
)
