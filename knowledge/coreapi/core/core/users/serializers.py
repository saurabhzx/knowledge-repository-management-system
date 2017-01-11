from rest_framework import serializers
from django.contrib.auth.models import User

from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('contact_no',)


class UserSerializer(serializers.ModelSerializer):

    groups = serializers.SerializerMethodField('get_groups')

    def get_groups(self, obj):
        groups = []
        for g in obj.groups.all():
            groups.append(g.name)

        if obj.is_staff:
            groups.append('Staff')
        if obj.is_superuser:
            groups.append('SuperUser')
        return groups

    def to_native(self, obj):
        ret = super(UserSerializer, self).to_native(obj)
        print ret
        if not ret['first_name'] and not ret['last_name']:
            ret['first_name'] = "No"
            ret['last_name'] = "Name"
        ret['name'] = ret['first_name'] + " " + ret['last_name']
        return ret

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name',
                  'groups','is_active', 'last_login', 'date_joined')
        read_only_fields = ('is_active', 'last_login', 'date_joined')
        write_only_fields = ('password',)

