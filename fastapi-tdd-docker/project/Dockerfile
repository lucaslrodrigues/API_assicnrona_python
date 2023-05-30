FROM python:3.11.2-slim-buster

WORKDIR /usr/src/app

# Impede que Python grave arquivos pyc no disco (equivalente à opçãopython -B)
ENV PYTHONDONTWRITEBYTECODE 1 

# PYTHONUNBUFFERED: Impede que o Python armazene em buffer stdout e stderr (equivalente à opçãopython -u)
ENV PYTHONUNBUNFERED 1

RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .