FROM mcr.microsoft.com/devcontainers/python:3.11

ARG USER=vscode

# Python and poetry installation
USER $USER
ENV PATH="/home/$USER/.local/bin:$PATH"

RUN curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.in-project true
