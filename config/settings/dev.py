"""開発用サーバーで使用する設定ファイル。

runserver時の起動オプションに「--settings=config.settings.dev」を追加するか、
環境変数に「DJANGO_SETTINGS_MODULE=config.settings.dev」を設定すると使用できる。
"""
# ruff: noqa
import os

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    default="django-insecure-(5zv^%pip&7%x*6*xa7t2j^6ut&kbqqei1ebkw2^p^dg%zb!2w",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

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
# 設定されていなければ*.onrender.comのホスト名になる。
SITE_DOMAIN = ALLOWED_HOSTS[0]

# django-debug-toolbar
INSTALLED_APPS.append("debug_toolbar")
MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = BASE_DIR / "staticfiles"
