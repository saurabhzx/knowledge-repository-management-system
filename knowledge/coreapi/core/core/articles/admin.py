from django.contrib import admin

from .models import Article, ArticleAnalytic, ArticleFollower, ArticleVote, ArticleRate, ArticleTag


"""
This is admin panel for Article
"""


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'owner','file',)
    list_display_links = ('id', 'owner')
    search_fields = ('title', 'owner__username')


"""
This is admin panel for Article analytics
"""


class ArticleAnalyticAdmin(admin.ModelAdmin):
    list_display = ('article', 'views', 'likes', 'average_rating',
                    'no_of_raters', 'no_of_followers', 'up_vote', 'down_vote',)
    list_display_links = ('article',)
    search_fields = ('title', 'article__title')

"""
This is admin panel for Article followers
"""


class ArticleFollowerAdmin(admin.ModelAdmin):
    list_display = ('article', 'users',)
    list_display_links = ('article', 'users')
    search_fields = ('article__title', 'users__username')


"""
This is admin panel for Article vote
"""


class ArticleVoteAdmin(admin.ModelAdmin):
    list_display = ('article', 'users', 'vote',)
    list_display_links = ('article', 'users')
    search_fields = ('article__title', 'users__username')


"""
This is admin panel for Article rate
"""


class ArticleRateAdmin(admin.ModelAdmin):
    list_display = ('article', 'users', 'rating',)
    list_display_links = ('article', 'users')
    search_fields = ('article__title', 'users__username')

"""
This is admin panel for Article tags
"""


class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleAnalytic, ArticleAnalyticAdmin)
admin.site.register(ArticleFollower, ArticleFollowerAdmin)
admin.site.register(ArticleVote, ArticleVoteAdmin)
admin.site.register(ArticleRate, ArticleRateAdmin)
admin.site.register(ArticleTag, ArticleTagAdmin)
