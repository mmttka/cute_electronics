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
        # 内部処理全般
        "django": {
            "handlers": ["file"],
            "level": "INFO"
        },
        # my_creationsアプリのロガー
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
            'when': 'D',  # ログローテーション(新しいファイルへの切り替え)間隔の単位(D=日)
            'interval': 1,  # ログローテーション間隔(1日単位)
            'backupCount': 7,  # 保存しておくログファイル数
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

