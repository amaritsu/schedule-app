"""CircleCIで使用する設定ファイル"""
# ruff: noqa
import os

from .base import *

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    default="django-insecure-(5zv^%pip&7%x*6*xa7t2j^6ut&kbqqei1ebkw2^p^dg%zb!2w",
)

DEBUG = False

WSGI_APPLICATION = "config.wsgi.application"

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "circle_test",
        "USER": "circleci",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "5432",
        "TEST": {"NAME": "custom_test_database"},
    }
}

STATICFILE_DIRS = [BASE_DIR / "static"]
MEDIA_ROOT = BASE_DIR / "media"
