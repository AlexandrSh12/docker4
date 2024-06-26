FROM python:3.11-alpine

# configure Poetry
ENV POETRY_VERSION=1.7.1
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

# install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
	&& $POETRY_VENV/bin/pip install -U pip setuptools \
	&& $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# add poetry to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR .

COPY . .

# install dependencies
RUN poetry install

RUN poetry run alembic upgrade head
CMD poetry run gunicorn app.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000