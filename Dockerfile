FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

COPY requirements/*.txt ./

RUN pip3 install --upgrade pip \
    && pip3 install -r prod.txt

ADD ./src/app /code/app
ADD ./src/manage.py /code/manage.py
WORKDIR /code

ENV PYTHONPATH=/code

CMD python manage.py runserver