"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append('/home/ubuntu/coreapi/core')
sys.path.append('/home/ubuntu/.local/lib/python2.7/dist-packages')
sys.path.append('/usr/local/lib/python2.7/dist-packages')
os.environ['DJANGO_DEBUG'] = 'False'
os.environ['MYSQL_USER'] = 'root'
os.environ['MYSQL_PASSWORD'] = 'xxxx'
os.environ['MYSQL_HOST'] = 'xxxx'
os.environ['MYSQL_PORT'] = 'xxxx'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
