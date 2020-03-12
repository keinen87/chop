
FROM python:3.7

MAINTAINER nurbek@inbox.ru

RUN apt-get clean && apt-get update && apt-get install -y python-pip

ADD . /usr/src/app
WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
    
CMD exec gunicorn chop.wsgi:application --bind 0.0.0.0:8000 --workers 3