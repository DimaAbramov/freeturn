FROM python:3.7.5
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y install build-essential
RUN pip install --upgrade pip && pip install --upgrade pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
COPY Pipfile.lock Pipfile.lock
RUN pipenv install --system --deploy --ignore-pipfile --dev

WORKDIR /app
COPY . /app

RUN python manage.py migrate
RUN pytest -n auto

ENTRYPOINT bash
