from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User

from core.search.models import QuestionQueryset

"""
This model contain all the Questions detail posted by the User
"""

class Question(models.Model):
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
    created_on = models.DateTimeField(auto_now_add=True)

    objects = QuestionQueryset.as_manager()

    def __unicode__(self):
        return u'%s. %s' % (
            self.id, self.title)


"""
This model contain all the analytics related to question
"""


class QuestionAnalytic(models.Model):
    question = models.OneToOneField(
        Question,
        primary_key=True,
        related_name="question_analytics")
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    average_rating = models.IntegerField(default=0)
    no_of_raters = models.IntegerField(default=0)
    no_of_followers = models.IntegerField(default=0)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s |%s views: %s no_of_followers: %s likes: %s up_votes: %s down_votes: %s average_rating: ' % (self.question.title,
                                                                                                                 self.views,
                                                                                                                 self.no_of_followers,
                                                                                                                 self.likes,
                                                                                                                 self.up_vote,
                                                                                                                 self.down_vote,
                                                                                                                 self.average_rating)

"""
This model keep track of number of followers of a question
"""


class QuestionFollower(models.Model):
    question = models.ForeignKey(Question)
    users = models.ForeignKey(User)
    followed_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s | %s | %s' % (self.question.title, self.users.username, self.followed_on)


"""
This model keep track of number of likes of a question
"""


class QuestionVote(models.Model):
    UP = 1
    DOWN = 0
    STATUS_CHOICES = (
        (UP, 'Up'),
        (DOWN, 'Down'),
    )
    question = models.ForeignKey(Question)
    users = models.ForeignKey(User)
    vote = models.IntegerField(default=0, choices=STATUS_CHOICES)
    voted_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s | %s | %s' % (self.question.title, self.users.username, self.vote)


"""
This model keep track the rating of a question
"""


class QuestionRate(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    question = models.ForeignKey(Question)
    users = models.ForeignKey(User)
    rating = models.IntegerField(default=0, choices=RATING_CHOICES)
    rated_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s | %s | %s' % (self.question.title, self.users.username, self.rating)


"""
This model contains the tags related to the question
"""


class QuestionTag(models.Model):
    questions = models.ManyToManyField(
        Question, blank=True, null=True)
    name = models.CharField(max_length=100, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.name)
