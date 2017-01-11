from django.conf.urls import *

from .views import QuestionList, QuestionDetail, QuestionAnalyticDetail, QuestionTagList


urlpatterns = patterns(
    '',
    url(r'^$', QuestionList.as_view(), name='question-list'),
    url(r'^/(?P<question__pk>[0-9]+)$',
        QuestionDetail.as_view(), name='question-detail'),
        url(r'^/(?P<question__pk>[0-9]+)/analytics$',
        QuestionAnalyticDetail.as_view(), name='analytics-question'),
	url(r'^/(?P<question__pk>[0-9]+)/tags$', QuestionTagList.as_view(), name='tag-list'),
)
