FROM python:3.11

ARG DATABASE_URL DJANGO_SETTINGS_MODULE SECRET_KEY RENDER_EXTERNAL_HOSTNAME

ENV PYTHONUNBUFFERED=1 PATH="${PATH}:/root/.local/bin"

# ワークディレクトリの設定
WORKDIR /code

# Poetryのインストール
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.create false

# Poetryの設定とlockファイルを/code/にコピーする
COPY pyproject.toml poetry.lock /code/

# Pythonの依存関係をインストール
RUN poetry install --only main

COPY . /code/

# 起動
RUN python manage.py collectstatic --noinput && \
    python manage.py migrate --noinput

EXPOSE 8000

CMD [ "gunicorn", "config.wsgi:application" ]
