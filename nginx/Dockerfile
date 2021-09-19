FROM nginx:1.21.3-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx/nginx.tmpl /etc/nginx/conf.d
# Review response (TODO: delete afterwards): название файла c расширением tmpl
# выбрано не случайно, это шаблон для генерации конфига nginx в зависимости
# от соответствующих настроек DJANGO_APP_PORT и NGINX_PORT в окружении.
# Соответствующая инструкция содержится в Dockercompose. Выделять целый volume
# для одного конфигурационного файла представляется излишним. Файл default.conf 
# в проекте я использую дефолтный.

ENV HOME=/home
ENV APP_HOME=/home/app
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
WORKDIR $APP_HOME