import datetime
import string

from django.conf import settings
from django.db.models import Max
from django.template.loader import render_to_string
from django.contrib.auth.models import User, Group
from django.db import models
from django.db import transaction
from django.utils.translation import ugettext_lazy as _

from .tasks import *

# Create your models here.

class UserProfileManager(models.Manager):

    def create_inactive_user(self, username, email, password,first_name, last_name,
                        send_email=True):
        new_user = User.objects.create_user(username, email, password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.is_active = True
        new_user.save()

        user_profile = self.create_profile(new_user)

        associate_group, created = Group.objects.get_or_create(name='Associate')
        new_user.groups.add(associate_group)
        send_welcome_message.delay(new_user)

        return new_user


    def create_profile(self, user):
        """
        Create a ``RegistrationProfile`` for a given
        ``User``, and return the ``RegistrationProfile``.

        The activation key for the ``RegistrationProfile`` will be a
        SHA1 hash, generated from a combination of the ``User``'s
        username and a random salt.
        salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
        username = user.username
        if isinstance(username, unicode):
            username = username.encode('utf-8')
        activation_key = hashlib.sha1(salt + username).hexdigest()"""
        return self.create(user=user,contact_no=user.username)

    def send_welcome_message(self, user):
        ctx_dict = {'owner': user.username,
                    'self': self}
        # Email subject *must not* contain newlines
        subject = 'Welcome to Knowledge Platform'
        message = render_to_string('welcome_message.txt',
                                   ctx_dict)
        user.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name="user")
    contact_no = models.CharField(max_length=10, unique=True)

    objects = UserProfileManager()
