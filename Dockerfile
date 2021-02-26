FROM python:3.7-alpine

LABEL maintainer="Lee Forster"
LABEL version="1.0.0"

COPY ./requirements.txt /requirements.txt 

RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev

RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app

COPY . /app

RUN adduser -D user
USER user