import os 

from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User

from core.search.models import ArticleQueryset


def content_file_name(instance, filename):
    fileName, fileExtension = os.path.splitext(filename)
    print fileExtension
    print instance
    return 'archive/' + str(instance.owner.pk) +'/' + filename


"""
This model contain all the Article detail posted by the User
"""


class Article(models.Model):
    INACTIVE = 0
    PUBLISHED = 1
    STATUS_CHOICES = (
        (INACTIVE, 'Inactive'),
        (PUBLISHED, 'Published'),
    )
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=500, blank=True, null=False)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)
    file = models.FileField(upload_to=content_file_name, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    objects = ArticleQueryset.as_manager()

    def file_url(self):
        if(self.id is not None and self.file):
            return self.file.url
        else:
            return "%s%s" % (settings.STATIC_URL, 'empty_cover.png')

    def __unicode__(self):
        return u'%s. %s' % (
            self.id, self.title)


"""
This model contain all the analytics related to article
"""


class ArticleAnalytic(models.Model):
    article = models.OneToOneField(
        Article,
        primary_key=True,
        related_name="article_analytics")
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    average_rating = models.IntegerField(default=0)
    no_of_raters = models.IntegerField(default=0)
    no_of_followers = models.IntegerField(default=0)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s |%s views: %s no_of_followers: %s likes: %s up_votes: %s down_votes: %s average_rating: ' % (self.article.title,
                                                                                                                 self.views,
                                                                                                                 self.no_of_followers,
                                                                                                                 self.likes,
                                                                                                                 self.up_vote,
                                                                                                                 self.down_vote,
                                                                                                                 self.average_rating)


"""
This model keep track of number of followers of a article
"""


class ArticleFollower(models.Model):
    article = models.ForeignKey(Article)
    users = models.ForeignKey(User)
    followed_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s | %s | %s' % (self.article.title, self.users.username, self.followed_on)


"""
This model keep track of number of likes of a article
"""


class ArticleVote(models.Model):
    UP = 1
    DOWN = 0
    STATUS_CHOICES = (
        (UP, 'Up'),
        (DOWN, 'Down'),
    )
    article = models.ForeignKey(Article)
    users = models.ForeignKey(User)
    vote = models.IntegerField(default=0, choices=STATUS_CHOICES)
    voted_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s | %s | %s' % (self.article.title, self.users.username, self.vote)


"""
This model keep track the rating of a article
"""


class ArticleRate(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    article = models.ForeignKey(Article)
    users = models.ForeignKey(User)
    rating = models.IntegerField(default=0, choices=RATING_CHOICES)
    rated_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s | %s | %s' % (self.article.title, self.users.username, self.rating)


"""
This model contains the tags related to the article
"""


class ArticleTag(models.Model):
    articles = models.ManyToManyField(
        Article, blank=True, null=True)
    name = models.CharField(max_length=100, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.name)
