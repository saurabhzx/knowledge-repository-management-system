from django.conf.urls import *

from .views import (UserList, UserDetail, UserMe, UserAuthToken)

urlpatterns = patterns(
    '',
    url(r'^$', UserList.as_view(), name='user-list'),
    url(r'^/me$', UserMe.as_view(), name='user-me'),
    url(r'^/(?P<user__pk>[0-9]+)$', UserDetail.as_view(), name='user-detail'),
    url(r'^/authenticate/(?P<backend>\w+)$', UserAuthToken.as_view(), name='user-auth'),
)
