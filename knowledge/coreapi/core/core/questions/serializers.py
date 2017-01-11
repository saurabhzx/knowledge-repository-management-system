from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum

from rest_framework import serializers

from .models import Question, QuestionAnalytic, QuestionFollower, QuestionTag

from core.question_answers.models import Answer
from core.question_answers.serializers import AnswerSerializer

"""
Serializer for question
"""


class QuestionSerializer(serializers.ModelSerializer):
    owner_name = serializers.Field(source='owner.username')
    question_analytic = serializers.SerializerMethodField('get_analytic')
    tags = serializers.SerializerMethodField('get_tags')

    class Meta:
        model = Question
        fields = ('id', 'title', 'description','owner',
                  'status', 'owner_name', 'created_on','question_analytic','tags',)
        read_only_fields = ('id', 'status','created_on',)

    def get_analytic(self,obj):
        question_analytic = QuestionAnalytic.objects.get(question__pk=obj.pk)
        serializers = QuestionAnalyticSerializer(question_analytic)
        return serializers.data

    def get_tags(self,obj):
        tags_details = QuestionTag.objects.filter(questions__pk=obj.pk)
        tags = ""
        for obj in tags_details:
            tags = tags + "," + obj.name
        tags = fixed = tags[1:]
        return tags


"""
Serializer for question
"""


class QuestionDetailSerializer(serializers.ModelSerializer):
    owner_name = serializers.Field(source='owner.username')
    answers = serializers.SerializerMethodField('get_comments')
    question_analytic = serializers.SerializerMethodField('get_analytic')
    tags = serializers.SerializerMethodField('get_tags')

    class Meta:
        model = Question
        fields = ('id', 'title', 'description','owner',
                  'status', 'owner_name', 'created_on','answers','question_analytic','tags',)
        read_only_fields = ('id', 'status','created_on','owner')

    def get_comments(self,obj):
        answers_details = Answer.objects.filter(question__pk=obj.pk)
        answers= []
        for obj in answers_details:
            answers.append(obj)
        serializers = AnswerSerializer(answers, many=True)
        return serializers.data

    def get_analytic(self,obj):
        question_analytic = QuestionAnalytic.objects.get(question__pk=obj.pk)
        serializers = QuestionAnalyticSerializer(question_analytic)
        question_analytic.views+=1
        question_analytic.save()
        return serializers.data

    def get_tags(self,obj):
        tags_details = QuestionTag.objects.filter(questions__pk=obj.pk)
        tags = ""
        for obj in tags_details:
            tags = tags + "," + obj.name
        tags = fixed = tags[1:]
        return tags


"""
Serializer for question analytics
"""


class QuestionAnalyticSerializer(serializers.ModelSerializer):
    question_title = serializers.Field(source='question.title')

    class Meta:
        model = QuestionAnalytic
        fields = ('question_title', 'views',
                  'likes', 'average_rating', 'no_of_followers','up_vote','down_vote','created_on',)


"""
Serializer for question followers
"""


class QuestionFollowerSerializer(serializers.ModelSerializer):
    question_title = serializers.Field(source='question.title')
    users_name = serializers.Field(source='users.username')

    class Meta:
        model = QuestionFollower
        fields = ('question_title', 'users_name',
                  'followed_on',)


"""
Serializer for question tags
"""


class QuestionTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionTag
        exclude = ('questions',)