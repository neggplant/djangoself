"""
Django settings for djangoself project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import sys
from urllib.parse import quote

from kombu import Queue, Exchange

from conf.env import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v=+rn3_lflzervi#e!u!(a+y34t$%0dz^bznkfe^-ocp3)^4nk'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'apps.baseapp',
    'apps.djapp',
    'apps.drfapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'application.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'application.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if DEBUG:
    # Django Debug Toolbar 设置
    INSTALLED_APPS += ["debug_toolbar"]
    MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE
    INTERNAL_IPS = ['127.0.0.1', ]

    # this is the main reason for not showing up the toolbar
    import mimetypes

    mimetypes.add_type("application/javascript", ".js", True)
    mimetypes.add_type("text/css", ".css", True)
    mimetypes.add_type("text/javascript", ".js", True)

    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda request: False if request.is_ajax() else True,
        "INTERCEPT_REDIRECTS": False,
    }

if OPEN_SILK:
    INSTALLED_APPS += ['silk']
    MIDDLEWARE += ['silk.middleware.SilkyMiddleware']
    # True：使用Python的内置cProfile分析器
    SILKY_PYTHON_PROFILER = True
    # 生成.prof文件，silk产生的程序跟踪记录，详细记录来执行的文件，行，时间等信息
    SILKY_PYTHON_PROFILER_BINARY = False
    if sys.platform == "win32":
        SILK_RESULT_PATH = os.path.join(BASE_DIR, 'log', 'silk', 'profiles')
    else:
        SILK_RESULT_PATH = os.path.join(os.getenv("SILK_RESULT_PATH", "/var/log"), 'silk', "profiles")
    os.makedirs(SILK_RESULT_PATH, exist_ok=True)
    # 如果没有本设置，prof文件将默认保存在MEDIA_ROOT里
    SILKY_PYTHON_PROFILER_RESULT_PATH = SILK_RESULT_PATH

if DEBUG:
    INSTALLED_APPS += ['drf_yasg']

    SWAGGER_SETTINGS = {
        'SECURITY_DEFINITIONS': {
            'basic': {
                'type': 'basic'
            }
        },
    }

    REDOC_SETTINGS = {
        'LAZY_RENDERING': False,
    }

if DATABASE_TYPE == "MYSQL":
    # Mysql数据库
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "HOST": os.getenv('DATABASE_HOST') or DATABASE_HOST,
            "PORT": os.getenv('DATABASE_PORT') or DATABASE_PORT,
            "USER": os.getenv('DATABASE_USER') or DATABASE_USER,
            "PASSWORD": os.getenv('DATABASE_PASSWORD') or DATABASE_PASSWORD,
            "NAME": os.getenv('DATABASE_NAME') or DATABASE_NAME,
        }
    }
else:
    # sqlite3 数据库
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# 是否使用redis集群
if IS_REDIS_CLUSTER:
    REDIS_LOCATION = 'redis://:{}@{}:{}/{}'.format(quote(REDIS_PASSWORD), REDIS_HOST, REDIS_PORT, REDIS_DB)
    REDIS_CLIENT_CLASS = 'redis.RedisCluster'
    CONNECTION_POOL_CLASS = 'redis.ConnectionPool'
    CONNECTION_POOL_KWARGS = {'skip_full_coverage_check': True, 'decode_components': True, 'max_connections': 200}
else:
    # quote和decode_components为防止redis密码中带有#?等特殊字符
    REDIS_LOCATION = 'redis://:{}@{}:{}/{}'.format(quote(REDIS_PASSWORD), REDIS_HOST, REDIS_PORT, REDIS_DB)
    REDIS_CLIENT_CLASS = 'redis.client.StrictRedis'
    CONNECTION_POOL_CLASS = 'redis.connection.ConnectionPool'
    CONNECTION_POOL_KWARGS = {'decode_components': True}

# 是否启用redis
if locals().get("REDIS_ENABLE", True):
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": REDIS_LOCATION,
            'REDIS_CLIENT_CLASS': REDIS_CLIENT_CLASS,
            'CONNECTION_POOL_CLASS': CONNECTION_POOL_CLASS,
            'CONNECTION_POOL_KWARGS': CONNECTION_POOL_KWARGS,
            "DECODE_RESPONSES": True
        },
    }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'application.utils.exception.custom_exception_handler'
}

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

"""
Celery配置
"""
# rabbit server
RABBIT_HOST = os.getenv('RABBIT_HOST', '127.0.0.1')
RABBIT_PORT = os.getenv('RABBIT_PORT', 5672)
RABBIT_USER = os.getenv('RABBIT_USER', 'rabbit')
RABBIT_PASSWORD = os.getenv('RABBIT_PASSWORD', 'rabbit')
RABBIT_VHOST = os.getenv('RABBIT_VHOST', "/")

# Celery
# todo:若使用redis集群，将celery结果存入Mysql，
BROKER_BACKEND_URL = 'redis://:{}@{}:{}/{}'.format(quote(REDIS_PASSWORD), REDIS_HOST, REDIS_PORT, REDIS_DB)
BROKER_URL = 'amqp://{user}:{password}@{host}:{port}/{vhost}'.format(
    user=RABBIT_USER,
    password=RABBIT_PASSWORD,
    host=RABBIT_HOST,
    port=RABBIT_PORT,
    vhost=RABBIT_VHOST
)
CELERY_BROKER_URL = BROKER_URL
CELERY_RESULT_BACKEND = BROKER_BACKEND_URL
# CELERY_RESULT_PERSISTENT = False
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Shanghai'
# CELERY_ENABLE_UTC = True,
# CELERY_CREATE_MISSING_QUEUES = True
# CELERYD_FORCE_EXECV = True  # 有些情况下可以防止死锁
CELERY_WORKER_PREFETCH_MULTIPLIER = 3
# CELERY_TASK_TRACK_STARTED = False
# CELERYD_MAX_TASKS_PER_CHILD = 50
# CELERY_TASK_RESULT_EXPIRES = 24 * 60 * 60
# CELERY_BROKER_HEARTBEAT = 0
# CELERY_BROKER_POOL_LIMIT = 0
CELERY_DEFAULT_QUEUE = "djangoself"
# CELERY_QUEUES = (
#     # Queue('celery', exchange=Exchange('celery'), routing_key='celery'),
#     Queue(CELERY_DEFAULT_QUEUE, exchange=Exchange(CELERY_DEFAULT_QUEUE), routing_key=CELERY_DEFAULT_QUEUE),
# )


"""
日志配置
"""
# log 配置部分BEGIN #
APPS_LOGS_FILE = os.path.join(BASE_DIR, 'logs', 'apps.log')
ERROR_LOGS_FILE = os.path.join(BASE_DIR, 'logs', 'error.log')
DB_LOGS_FILE = os.path.join(BASE_DIR, 'logs', 'db.log')
SERVER_LOGS_FILE = os.path.join(BASE_DIR, 'logs', 'server.log')
# make folder of logs
if not os.path.exists(os.path.join(BASE_DIR, 'logs')):
    os.makedirs(os.path.join(BASE_DIR, 'logs'))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'standard': {
            'format': '%(asctime)s.%(msecs)d [%(levelname)s] [%(name)s] [%(filename)s:%(lineno)s] [%(funcName)s] '
                      '%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            # not use level here, it is an error config.
            'level': 'DEBUG',
            # 'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'apps': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': APPS_LOGS_FILE,
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 5,
            'formatter': 'standard'
        },
        'db': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': DB_LOGS_FILE,
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 5,
            'formatter': 'standard'
        },
        'server': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': SERVER_LOGS_FILE,
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 5,
            'formatter': 'standard'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', "server"],
            # default INFO if no level
            'level': 'DEBUG',
        },
        'apps': {
            'handlers': ["apps"],
            'level': 'DEBUG',
        },
        'django.db': {
            'handlers': ['db'],
            'level': 'DEBUG',
        },
    }
}
