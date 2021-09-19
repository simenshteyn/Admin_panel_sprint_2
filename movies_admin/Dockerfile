FROM python:3.9-alpine

ADD ./movies_admin/requirements.txt /app/requirements.txt

ADD ./sqlite_to_postgres/db.sqlite /app/db.sqlite
ADD ./sqlite_to_postgres/load_data.py /app/load_data.py
# Review Response (TODO: delete afterwards) данный образ используется для
# установки зависимостей, первоначальной настройки Django, и загрузки данных.
# Для этих целей служит контейнер django_startapp, инструкции объеденины в
# один блок, поскольку это разовая операция. Кроме того, файлы load_data и
# db.sqlite удаляются после первоначальной уставки.

RUN apk add --no-cache bash

RUN set -ex \
    && apk add --no-cache --virtual .build-deps postgresql-dev build-base \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /app/requirements.txt \
    && runDeps="$(scanelf --needed --nobanner --recursive /env \
        | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
        | sort -u \
        | xargs -r apk info --installed \
        | sort -u)" \
    && apk add --virtual rendeps $runDeps \
    && apk del .build-deps

RUN apk add curl
# Review Respose (TODO: delete afterwards) данная зависимость не является лишней.
# Curl используется для мониторинга состояния контейнера через healthcheck.

ADD ./movies_admin /app
WORKDIR /app

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH
# Review Response (TODO: delete afterwards) запуск проекта не входит в задачи
# данного Dockerfile. Запуск проекта производится в docker-compose.yml (24 стр),
# поскольку это отдельная задача, не связанная с первоначальным развертыванием.