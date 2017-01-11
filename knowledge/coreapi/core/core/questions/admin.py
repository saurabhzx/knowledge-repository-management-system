from django.contrib import admin

from .models import Question, QuestionAnalytic, QuestionFollower, QuestionVote, QuestionRate, QuestionTag


"""
This is admin panel for Question
"""


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'owner',)
    list_display_links = ('id', 'owner')
    search_fields = ('title', 'owner__username')


"""
This is admin panel for question analytics
"""


class QuestionAnalyticAdmin(admin.ModelAdmin):
    list_display = ('question', 'views', 'likes', 'average_rating',
                    'no_of_raters', 'no_of_followers', 'up_vote', 'down_vote',)
    list_display_links = ('question',)
    search_fields = ('title', 'question__title')

"""
This is admin panel for question followers
"""


class QuestionFollowerAdmin(admin.ModelAdmin):
    list_display = ('question', 'users',)
    list_display_links = ('question', 'users')
    search_fields = ('question__title', 'users__username')


"""
This is admin panel for question vote
"""


class QuestionVoteAdmin(admin.ModelAdmin):
    list_display = ('question', 'users', 'vote',)
    list_display_links = ('question', 'users')
    search_fields = ('question__title', 'users__username')


"""
This is admin panel for question rate
"""


class QuestionRateAdmin(admin.ModelAdmin):
    list_display = ('question', 'users', 'rating',)
    list_display_links = ('question', 'users')
    search_fields = ('question__title', 'users__username')

"""
This is admin panel for question tags
"""


class QuestionTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionAnalytic, QuestionAnalyticAdmin)
admin.site.register(QuestionFollower, QuestionFollowerAdmin)
admin.site.register(QuestionVote, QuestionVoteAdmin)
admin.site.register(QuestionRate, QuestionRateAdmin)
admin.site.register(QuestionTag, QuestionTagAdmin)
