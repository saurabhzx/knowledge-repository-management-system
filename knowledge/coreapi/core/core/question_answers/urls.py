
from django.conf.urls import *

from .views import AnswerList, AnswerDetail


urlpatterns = patterns(
    '',
    url(r'^/question/(?P<question__pk>[0-9]+)$', AnswerList.as_view(), name='answer-list'),
)
