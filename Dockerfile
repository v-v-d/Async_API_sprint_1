FROM python:3.9-slim AS base
ENV PYTHONUNBUFFERED 1
COPY requirements/*.txt ./


FROM base AS prod
RUN pip3 install -r prod.txt

ADD ./src/app /code/app
ADD ./src/manage.py /code/manage.py
WORKDIR /code

ENV PYTHONPATH=/code

CMD python manage.py runserver


FROM base AS tests
COPY src/tests/functional/requirements.txt ./

RUN pip3 install -r requirements.txt

ADD ./src /code
WORKDIR /code

ENV PYTHONPATH=/code

CMD pytest -p no:warnings --cov-report term-missing --cov=/code/app /code/tests