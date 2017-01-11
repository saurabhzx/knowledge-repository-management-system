from __future__ import absolute_import

from celery.decorators import task
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


@task()
def send_welcome_message(user):
    ctx_dict = {'owner': user.username}
    # Email subject *must not* contain newlines
    subject = 'Welcome to Knowledge Platform'
    message = render_to_string('welcome_message.txt',
                               ctx_dict)
    user.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)