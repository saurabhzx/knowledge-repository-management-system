from django.contrib import admin

from .models import Answer, AnswerAnalytic, AnswerVote


"""
This is admin panel for Answer
"""


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer', 'user_answer',)
    list_display_links = ('question', 'user_answer')
    search_fields = ('question__title', 'user_answer__username')

"""
This is admin panel for AnswerAnalytic
"""


class AnswerAnalyticAdmin(admin.ModelAdmin):
    list_display = ('answer', 'up_vote', 'down_vote',)
    list_display_links = ('answer',)
    search_fields = ('answer__answer',)

"""
This is admin panel for AnswerAnalytic
"""


class AnswerVoteAdmin(admin.ModelAdmin):
    list_display = ('answer', 'users', 'vote')
    list_display_links = ('answer', 'users',)
    search_fields = ('answer__answer', 'users__username')

admin.site.register(Answer, AnswerAdmin)
admin.site.register(AnswerAnalytic, AnswerAnalyticAdmin)
admin.site.register(AnswerVote, AnswerVoteAdmin)
