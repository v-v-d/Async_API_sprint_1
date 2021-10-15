FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

COPY requirements/*.txt ./

RUN pip3 install --upgrade pip \
    && pip3 install -r prod.txt

ADD ./src /app
WORKDIR /app

ENV PYTHONPATH=/app

CMD python manage.py runserver