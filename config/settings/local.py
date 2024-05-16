"""ローカルで使用する設定ファイル。

runserver時の起動オプションに「--settings=config.settings.local」を追加するか、
環境変数に「DJANGO_SETTINGS_MODULE=config.settings.local」を設定すると使用できる。
また、設定ファイルを指定せずに起動した場合もこのファイルが使われる。
"""
# ruff: noqa
import os
import sys

from django.contrib.messages import constants as messages_constants

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    default="django-insecure-(5zv^%pip&7%x*6*xa7t2j^6ut&kbqqei1ebkw2^p^dg%zb!2w",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# サイトのドメイン
SITE_DOMAIN = "127.0.0.1:8000"

# django-debug-toolbar
INSTALLED_APPS.append("debug_toolbar")
MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
}

# django-extensions
INSTALLED_APPS.append("django_extensions")

# Emailを送信する代わりにコンソールに表示する
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# デバッグ用メッセージの表示
MESSAGE_LEVEL = messages_constants.DEBUG
