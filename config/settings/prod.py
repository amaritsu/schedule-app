"""本番用サーバーで使用する設定ファイル。

runserver時の起動オプションに「--settings=config.settings.prod」を追加するか、
環境変数に「DJANGO_SETTINGS_MODULE=config.settings.prod」を設定すると使用できる。

リリース前にチェック -> https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
"""
# ruff: noqa
import os

from .base import *

SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = False

ALLOWED_HOSTS = []
if "SITE_DOMAIN" in os.environ:
    ALLOWED_HOSTS.append(os.environ["SITE_DOMAIN"])
if "RENDER_EXTERNAL_HOSTNAME" in os.environ:
    ALLOWED_HOSTS.append(os.environ["RENDER_EXTERNAL_HOSTNAME"])

CSRF_TRUSTED_ORIGINS = [
    host if host.startswith("https://") else f"https://{host}" for host in ALLOWED_HOSTS
]

# サイトのドメイン
# SITE_DOMAINの環境変数があれば、そのドメインを使用する。
# 設定されていなければonrender.comのホスト名になる。
SITE_DOMAIN = ALLOWED_HOSTS[0]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = BASE_DIR / "staticfiles"

# セキュリティ関連
# SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
