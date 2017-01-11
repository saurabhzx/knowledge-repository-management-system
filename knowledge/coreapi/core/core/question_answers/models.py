from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User

from core.questions.models import Question


"""
This model contain the answer of a question
"""


class Answer(models.Model):
    question = models.ForeignKey(Question)
    user_answer = models.ForeignKey(User)
    answer = models.CharField(max_length=100, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s | %s | %s' % (self.question.title, self.user_answer.username, self.answer)


"""
This model contain the answer analytics
"""


class AnswerAnalytic(models.Model):
    answer = models.OneToOneField(
        Answer,
        primary_key=True,
        related_name="answer_analytics")
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s | %s | %s' % (self.answer.answer, self.up_vote, self.down_vote)


"""
This model keep track of number of vote of a answer
"""


class AnswerVote(models.Model):
    UP = 1
    DOWN = 0
    STATUS_CHOICES = (
        (UP, 'up_vote'),
        (DOWN, 'down_vote'),
    )
    answer = models.ForeignKey(Answer)
    users = models.ForeignKey(User)
    vote = models.IntegerField(default=0, choices=STATUS_CHOICES)
    voted_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s | %s' % (self.answer.answer, self.users.username)
