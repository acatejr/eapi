FROM python:3.9.2
RUN apt-get update -y
RUN pip install poetry
RUN poetry config virtualenvs.create false

WORKDIR /opt/app
ADD poetry.lock .
ADD pyproject.toml .
ADD app/ .
ADD config.py .
ADD eapi.py .
ADD manage.py .
ADD tests/ .
RUN poetry install

