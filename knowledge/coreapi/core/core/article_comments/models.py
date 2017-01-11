from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User

from core.articles.models import Article


"""
This model contain the Comment of a Article
"""


class Comment(models.Model):
    article = models.ForeignKey(Article)
    user_comment = models.ForeignKey(User)
    comment = models.CharField(max_length=100, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s | %s | %s' % (self.article.title, self.user_comment.username, self.comment)


"""
This model contain the Comment analytics
"""


class CommentAnalytic(models.Model):
    comment = models.OneToOneField(
        Comment,
        primary_key=True,
        related_name="answer_analytics")
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s | %s | %s' % (self.comment.comment, self.up_vote, self.down_vote)


"""
This model keep track of number of vote of a Comment
"""


class CommentVote(models.Model):
    UP = 1
    DOWN = 0
    STATUS_CHOICES = (
        (UP, 'up_vote'),
        (DOWN, 'down_vote'),
    )
    comment = models.ForeignKey(Comment)
    users = models.ForeignKey(User)
    vote = models.IntegerField(default=0, choices=STATUS_CHOICES)
    voted_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s | %s' % (self.comment.comment, self.users.username)
