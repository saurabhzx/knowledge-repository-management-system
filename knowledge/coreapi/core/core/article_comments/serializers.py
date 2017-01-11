from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum

from rest_framework import serializers

from .models import Comment

"""
Serializer for comments
"""


class CommentSerializer(serializers.ModelSerializer):
    user_comment = serializers.Field(source='user_comment.username')

    class Meta:
        model = Comment
        fields = ('id','user_comment',
                  'comment', 'created_on',)
        read_only_fields = ('id','created_on',)


class CommentDetailSerializer(serializers.ModelSerializer):
    user_comment = serializers.Field(source='user_answer.username')

    class Meta:
        model = Comment
        fields = ('id','user_comment',
                  'answer', 'created_on',)
        read_only_fields = ('id','created_on',)