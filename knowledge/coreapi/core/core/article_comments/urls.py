
from django.conf.urls import *

from .views import CommentList, CommentDetail


urlpatterns = patterns(
    '',
    url(r'^/article/(?P<article__pk>[0-9]+)$', CommentList.as_view(), name='comments-list'),
)
