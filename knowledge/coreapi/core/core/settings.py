"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fr_4)upefvtq3+kqqabla$vm_j5&#u8(v4b9pgib@ik&7on$)&'

# SECURITY WARNING: don't run with debug turned on in production!

# Folder Path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            os.path.pardir))

environ_debug_var = os.environ.get('DJANGO_DEBUG', '1')

# no debug on production servers
if environ_debug_var == '0':
    DEBUG = False
else:
    DEBUG = True

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    #('Saurabh Bhatia', 'xyz@gmail.com'),
)

MANAGERS = ADMINS

production_base = ''
if not DEBUG:
    MEDIA_ROOT = os.path.join(production_base, 'media')
    STATIC_ROOT = os.path.join(production_base, 'static')
    STATIC_URL = ''
    MEDIA_URL = ''
    ADMIN_MEDIA_PREFIX = '/static/admin/'
else:
    MEDIA_ROOT = '/var/www/media/'
    STATIC_ROOT = '/var/www/static/'
    STATIC_URL = '/static/'
    MEDIA_URL = 'localhost/media/'
    ADMIN_MEDIA_PREFIX = 'localhost/admin/'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.humanize',

    'storages',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'corsheaders',
    'test_pep8',
    'sslserver',
    'celery',

    'core.users',
    'core.questions',
    'core.question_answers',
    'core.articles',
    'core.article_comments'
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # insert your TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

if DEBUG:

    DATABASES = {
        'default': {
            # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'ENGINE': 'django.db.backends.mysql',
            # Or path to database file if using sqlite3.
            'NAME': 'knowledge',
            'USER': 'root',
            'PASSWORD': 'saurabh',
            # Empty for localhost through domain sockets or '127.0.0.1' for
            # localhost through TCP.
            'HOST': '127.0.0.1',
            # Set to empty string for default.
            'PORT': '3306',
        }
    }

else:

    DATABASES = {
        'default': {
            # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'ENGINE': 'django.db.backends.mysql',
            # Or path to database file if using sqlite3.
            'NAME': 'knowledge',
            'USER': 'root',
            'PASSWORD': 'knowledge2511',
            # Empty for localhost through domain sockets or '127.0.0.1' for
            # localhost through TCP.
            'HOST': 'localhost',
            # Set to empty string for default.
            'PORT': '3306',
        }
    }


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'core.middleware.requirelogin.RequireLoginMiddleware',
    'maintenancemode.middleware.MaintenanceModeMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.middleware.django-crossdomainxhr-middleware.XsSharing',
)

# Static
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
)

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, 'core', 'templates'),
                 os.path.join(PROJECT_ROOT, 'core', 'templates'))

ALLOWED_HOSTS = ['*']
APPEND_SLASH = False
ROOT_URLCONF = 'core.urls'
LOGIN_URL = '/account/login'
LOGOUT_URL = '/account/logout'
LOGIN_REQUIRED_URLS = (
    # r'/(.*)$',
)

LOGIN_REQUIRED_URLS_EXCEPTIONS = (
    r'^/$',
    r'/admin(.*)$',
    r'/account(.*)$',
    r'/media(.*)$',
    r'/static(.*)$',
)


MAINTENANCE_IGNORE_URLS = (
    r'^/admin/.*',
)

MAINTENANCE_MODE = False
MAINTENANCE_IGNORE_URLS = (
    r'^/admin/.*',
    r'^/static/.*',
    r'^/media*'
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.JSONPRenderer',
        'rest_framework.renderers.XMLRenderer',
    )
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken'
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

TEST_PEP8_DIRS = [os.path.join(PROJECT_ROOT, 'core'), ]
TEST_PEP8_IGNORE = ['W191', 'E126', 'E501']  # W191 indentation contains tabs

""" For accessing UserProfile through user.getprofile()"""
AUTH_PROFILE_MODULE = "core.users.UserProfile"

# Email
ACCOUNT_ACTIVATION_DAYS = 7
EMAIL_HOST = 'localhost'
LOGIN_REDIRECT_URL = '/'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'test@gmail.com'
EMAIL_HOST_PASSWORD = '*********'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'test@gmail.com'
SERVER_EMAIL = 'test@gmail.com'

if not DEBUG:
    """ AWS secutity credentials """
    DEFAULT_FILE_STORAGE = 'core.s3utils.MediaRootS3BotoStorage'
    STATICFILES_STORAGE = 'core.s3utils.StaticRootS3BotoStorage'
    AWS_S3_HOST = 's3-ap-southeast-1.amazonaws.com'
    AWS_S3_SECURE_URLS = True       # use http instead of https
    # don't add complex authentication-related query parameters for requests
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_ACCESS_KEY_ID = '************'     # enter your access key id
    # enter your secret access key
    AWS_S3_SECRET_ACCESS_KEY = '************'
    AWS_STORAGE_BUCKET_NAME = '*********'
    # enter your default url of s3
    AWS_S3_CUSTOM_DOMAIN = '*********'


# Celery
BROKER_URL = 'amqp://guest:guest@localhost:5672//'
CELERY_RESULT_BACKEND = 'amqp://guest:guest@localhost:5672//'
CELERY_TASK_SERIALIZER = 'json'

if not DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
                'datefmt': "%d/%b/%Y %H:%M:%S"
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'file': {
                'level': 'ERROR',
                'filters': [],
                'class': 'logging.FileHandler',
                'filename': '/home/ubuntu/knowledge/logs/knowledge.log',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['file'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }
else:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
                'datefmt': "%d/%b/%Y %H:%M:%S"
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'file': {
                'level': 'ERROR',
                'filters': [],
                'class': 'logging.FileHandler',
                'filename': 'knowledge.log',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['file'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }