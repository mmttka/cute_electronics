from .settings_common import *



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-aix2pex8ytln7h-lk%#g$ckp2bt+5w=7)4ga+gm8anq5@p&vgl"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "'staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"




# ロギング設定
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False, # 既存のロガーを有効化

    # Loggerの設定
    "loggers": {
        # 内部処理全般
        "django": {
            "handlers": ["console"],
            "level": "INFO"
        },
        # my_creationsアプリのロガー
        "my_creations": {
            "handlers": ["console"],
            "level": "DEBUG"
        },
    },

    # Handlerの設定
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "dev",
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
