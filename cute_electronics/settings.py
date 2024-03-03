from .settings_common import *

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')]

STATIC_ROOT = 'usr/share/nginx/html/static'
MEDIA_ROOT = 'usr/share/nginx/html/media'

# ロギング設定
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    # Loggerの設定
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "INFO"
        },
        "my_creations": {
            "handlers": ["file"],
            "level": "INFO"
        },
    },

    # Handlerの設定
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter': 'prod',
            'when': 'D',
            'interval': 1,
            'backupCount': 7,
        },
    },


    # Formatterの設定
    "formatters":{
        "dev": {
            "format": '\t'.join([
                "%(asctime)s",
                "[%(levelname)s]",
                "%(pathname)s(Line:%(lineno)d)",
                "%(message)s"
            ])
        },
    }


}

