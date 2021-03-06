FROM python:3.9-slim

ENV APP_HOME=/app \
    # python:
    PYTHONDONTWRITEBYTECODE=1 \
    # pip:
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_NO_CACHE_DIR=off \
    # poetry:
    POETRY_HOME=/opt/poetry \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # virtualenv:
    VENV_PATH=/app/.venv

ENV PATH="${POETRY_HOME}/bin:${PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
WORKDIR ${APP_HOME}

COPY poetry.lock pyproject.toml entrypoint.sh ${APP_HOME}/

RUN set -ex \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        gcc \
        python3-dev \
    && curl -sSL 'https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py' | python \
    && poetry --version \
    && poetry install --no-dev\
    && sed -i 's/\r//' entrypoint.sh \
    && chown $USER:$USER entrypoint.sh \
    && chmod a+x entrypoint.sh

ENV VIRTUAL_ENV=/app/.venv
COPY . ${APP_HOME}/

EXPOSE 8000

ENTRYPOINT ["sh", "/app/entrypoint.sh"]
