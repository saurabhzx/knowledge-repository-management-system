from django.db import models


"""
Model Query set Full Text Search Article
"""
class ArticleQueryset(models.QuerySet):
    def text_search_name(self, name):
        return self.extra(
            select={'rank': "MATCH (title,description) AGAINST (%s IN NATURAL LANGUAGE MODE)"},
            select_params=(name,),
            where=('MATCH (title,description) AGAINST (%s IN NATURAL LANGUAGE MODE) > 0',),
            params=(name,),
            order_by=('-rank',)
        )


"""
Model Query set Full Text Search Article
"""
class QuestionQueryset(models.QuerySet):
    def text_search_name(self, name):
        return self.extra(
            select={'rank': "MATCH (title,description) AGAINST (%s IN NATURAL LANGUAGE MODE)"},
            select_params=(name,),
            where=('MATCH (title, description) AGAINST (%s IN NATURAL LANGUAGE MODE) > 0',),
            params=(name,),
            order_by=('-rank',)
        )