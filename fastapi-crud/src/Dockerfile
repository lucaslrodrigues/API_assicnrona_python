FROM python:3.11.0-alpine

WORKDIR /usr/src/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUNFFERED 1

COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN rm -rf /root/.cache/pip

COPY ./app /usr/src/