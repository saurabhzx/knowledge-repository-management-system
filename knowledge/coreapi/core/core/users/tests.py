import json

from django.contrib import auth
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group
from django.test import TestCase
from django.contrib.sites.models import Site
from django.contrib.auth.decorators import login_required
from django.test.client import Client
from rest_framework import status
from rest_framework.test import APITestCase, APISimpleTestCase
from rest_framework.test import APIClient, APIRequestFactory

from greedy.apps.account.models import *
from greedy.apps.account.views import *
from .serializers import UserSerializer
from .views import UserList, UserDetail


class UserProfileTestCase(APITestCase):

    def setUp(self):
        User.objects.create(username='lion', password='roar')
        self.client = Client()
        self.api_client = APIClient()

    def test_users_detail(self):
        """
        Fetch user details
        """
        user = User.objects.get(username='lion')
        url = reverse('user-detail', kwargs={'user__pk': user.pk})
        response = self.client.get(url, {}, format='json')
        groups = []
        for g in user.groups.all():
            groups.append(g.name)
        data = {'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'last_login': user.last_login,
                'date_joined': user.date_joined,
                'groups': groups,
                'is_active': user.is_active}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)

    def test_users_me(self):
        """ Anonymous User """
        url = reverse('user-me')
        response = self.client.get(url, {}, format='json')
        data = {
            'username': None,
            'first_name': 'Anonymous',
            'groups': [
                'Unsigned'
            ]
        }
        """ Logged in as Lion """
        user = User.objects.get(username='lion')
        self.api_client.force_authenticate(user=user)
        groups = []
        for g in user.groups.all():
            groups.append(g.name)
        data = {'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'last_login': user.last_login,
                'date_joined': user.date_joined,
                'groups': groups,
                'is_active': user.is_active}

        response = self.api_client.get(reverse('user-me'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)
