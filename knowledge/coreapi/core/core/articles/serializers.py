from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum

from rest_framework import serializers

from .models import Article, ArticleAnalytic, ArticleTag
from core.article_comments.models import Comment
from core.article_comments.serializers import CommentSerializer

"""
Serializer for question
"""


class ArticleSerializer(serializers.ModelSerializer):
    owner_name = serializers.Field(source='owner.username')
    file_url = serializers.Field(source='file_url')
    article_analytic = serializers.SerializerMethodField('get_analytic')
    article_tags = serializers.SerializerMethodField('get_tags')

    class Meta:
        model = Article
        fields = ('id', 'title', 'description','owner',
                  'status', 'owner_name', 'file_url', 'created_on','article_analytic','article_tags',)
        read_only_fields = ('id', 'status','created_on',)

    def get_analytic(self,obj):
        article_analytic = ArticleAnalytic.objects.get(article__pk=obj.pk)
        serializers = ArticleAnalyticSerializer(article_analytic)
        return serializers.data

    def get_tags(self,obj):
        tags_details = ArticleTag.objects.filter(articles__pk=obj.pk)
        tags = ""
        for obj in tags_details:
            tags = tags + "," + obj.name
        tags = fixed = tags[1:]
        return tags


"""
Serializer for article
"""


class ArticleDetailSerializer(serializers.ModelSerializer):
    owner_name = serializers.Field(source='owner.username')
    comments = serializers.SerializerMethodField('get_comments')
    article_analytic = serializers.SerializerMethodField('get_analytic')
    file_url = serializers.Field(source='file_url')
    tags = serializers.SerializerMethodField('get_tags')

    class Meta:
        model = Article
        fields = ('id', 'title', 'description','owner',
                  'status', 'owner_name', 'file_url','created_on','comments','article_analytic','tags',)
        read_only_fields = ('id', 'status','created_on','owner',)

    def get_comments(self,obj):
        comments_details = Comment.objects.filter(article__pk=obj.pk)
        comments= []
        for obj in comments_details:
            comments.append(obj)
        serializers = CommentSerializer(comments, many=True)
        return serializers.data

    def get_analytic(self,obj):
        article_analytic = ArticleAnalytic.objects.get(article__pk=obj.pk)
        serializers = ArticleAnalyticSerializer(article_analytic)
        article_analytic.views+=1
        article_analytic.save()
        return serializers.data

    def get_tags(self,obj):
        tags_details = ArticleTag.objects.filter(articles__pk=obj.pk)
        tags = ""
        for obj in tags_details:
            tags = tags + "," + obj.name
        tags = fixed = tags[1:]
        return tags


"""
Serializer for article analytics
"""


class ArticleAnalyticSerializer(serializers.ModelSerializer):
    article_title = serializers.Field(source='article.title')

    class Meta:
        model = ArticleAnalytic
        fields = ('article_title', 'views',
                  'likes', 'average_rating', 'no_of_followers','up_vote','down_vote','created_on',)


"""
Serializer for article tags
"""


class ArticleTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleTag
        exclude = ('articles',)