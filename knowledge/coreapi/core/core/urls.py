"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
admin.autodiscover()

urlpatterns = staticfiles_urlpatterns()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'coreapi.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       (r'^admin/', include(admin.site.urls)),

                       # Docs
                       url(r'^docs/', include('rest_framework_swagger.urls')),

                       url(r'^questions', include('core.questions.urls')),
                       url(r'^answers', include('core.question_answers.urls')),
                       url(r'^articles', include('core.articles.urls')),
                       url(r'^comments', include('core.article_comments.urls')),
                       url(r'^users', include('core.users.urls')),

                       )

urlpatterns = format_suffix_patterns(
    urlpatterns, allowed=['json', 'jsonp', 'xml'])
