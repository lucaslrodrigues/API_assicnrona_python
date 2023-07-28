FROM python:3.11.0-alpine

WORKDIR /usr/src/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUNFFERED 1

COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN rm -rf /root/.cache/pip
ENV DATABASE_URL "postgresql://postgres:postgres@db:5432/postgres"

COPY ./app /usr/src/