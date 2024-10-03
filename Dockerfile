FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
COPY ./animals /usr/src/app
COPY ./.env /usr/src

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000
