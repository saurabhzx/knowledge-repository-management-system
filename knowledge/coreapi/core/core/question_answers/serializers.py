from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum

from rest_framework import serializers

from .models import Answer

"""
Serializer for answer
"""

class AnswerSerializer(serializers.ModelSerializer):
    user_answer = serializers.Field(source='user_answer.username')

    class Meta:
        model = Answer
        fields = ('id','user_answer',
                  'answer', 'created_on',)
        read_only_fields = ('id','created_on',)


class AnswerDetailSerializer(serializers.ModelSerializer):
    user_answer = serializers.Field(source='user_answer.username')

    class Meta:
        model = Answer
        fields = ('id','user_answer',
                  'answer', 'created_on',)
        read_only_fields = ('id','created_on',)