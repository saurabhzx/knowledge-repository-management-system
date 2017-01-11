from django.contrib import admin

from .models import Comment, CommentAnalytic, CommentVote


"""
This is admin panel for Comment
"""


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'comment', 'user_comment',)
    list_display_links = ('article', 'user_comment')
    search_fields = ('article__title', 'user_comment__username')

"""
This is admin panel for CommentAnalytic
"""


class CommentAnalyticAdmin(admin.ModelAdmin):
    list_display = ('comment', 'up_vote', 'down_vote',)
    list_display_links = ('comment',)
    search_fields = ('comment__comment',)

"""
This is admin panel for CommentAnalytic
"""


class CommentVoteAdmin(admin.ModelAdmin):
    list_display = ('comment', 'users', 'vote')
    list_display_links = ('comment', 'users',)
    search_fields = ('comment__comment', 'users__username')

admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentAnalytic, CommentAnalyticAdmin)
admin.site.register(CommentVote, CommentVoteAdmin)
