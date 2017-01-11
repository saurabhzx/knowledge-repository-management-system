from django.conf import settings
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
from django.contrib.auth.models import User, Group
from django.contrib import auth
from django.http import Http404

from rest_framework.views import APIView
from rest_framework import status
from rest_framework import parsers
from rest_framework import renderers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer

from .serializers import UserSerializer

from .models import UserProfile


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    paginate_by = 12

    def post(self, request, *args, **kwargs):
        """
        Create new user
        """
        self.serializer_class = UserSerializer
        data = request.DATA
        print data
        serializer = UserSerializer(data=data)
        print serializer.data
        if serializer.is_valid():
            # serializer.save()
            username = data['username']
            email = data['email']
            password = data['password']
            first_name = data['first_name']
            last_name = data['last_name']
            if email and User.objects.filter(email=email).count() > 0 :
                return Response({"email": "This email address or username is already registered."},
                                status=status.HTTP_400_BAD_REQUEST)
            new_user = UserProfile.objects.create_inactive_user(username, email,
                                                                password, first_name, last_name)
            """signals.user_registered.send(sender=None,
                                         user=new_user,
                                         request=request)"""
            return Response({"message": "Please check your email address for activation link."},
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)


class UserDetail(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        try:
            user__pk = self.kwargs.get('user__pk', None)
            return User.objects.get(pk=user__pk)
        except:
            raise Http404

    def get_view_owner(self):
        return self.get_object()


    def post(self, request, *args, **kwargs):
        """
        Edit user details
        """
        user = self.get_object()
        print "i am here "
        print user
        print "now datra"
        data = request.DATA.copy()
        print data
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.set_password(data['password'])
        user.email = data['email'];
        user.username = data['username']
        user.save()
        return Response(data)


class UserMe(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_anonymous():
            return Response({'username': None,
                             'first_name': 'Anonymous',
                             'groups': ['Unsigned']})
        else:
            serializer = UserSerializer(user)
            return Response(serializer.data)


class UserAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (
        parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer
    model = Token

    # Accept backend as a parameter and 'auth' for a login / pass
    def post(self, request, backend):
        serializer = self.serializer_class(data=request.DATA)
        if serializer.is_valid():
            token, created = Token.objects.get_or_create(
                user=serializer.object['user'])
            return Response({'token': token.key})
        if 'non_field_errors' in serializer.errors:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)