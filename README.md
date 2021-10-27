[![Build Status](https://app.travis-ci.com/v-v-d/Async_API_sprint_1.svg?branch=main)](https://app.travis-ci.com/v-v-d/Async_API_sprint_1)

# API для кинотеатра

Точка входа для всех клиентов.

- Репозиторий для сервиса API: https://github.com/v-v-d/Async_API_sprint_1
- Репозиторий для сервиса ETL: https://github.com/v-v-d/ETL
- Доска: https://github.com/users/v-v-d/projects/3


### Основные сущности
- Фильм — заголовок, содержание, дата создания, возрастной ценз, режиссёры, актёры, сценаристы, жанры, ссылка на файл.
- Сериал — заголовок, содержание, даты создания, режиссёры, актёры, сценаристы, жанры, ссылка на файл.
- Актёр — имя, фамилия, фильмы с его участием.
- Режиссёр — имя, фамилия, фильмы, которые он снял.
- Сценарист — имя, фамилия, фильмы по его сценариям.
- Жанр — описание, популярность.

## Основные компоненты системы
- Cервер ASGI — сервер с запущенным приложением.
- Nginx — прокси-сервер, который является точкой входа для веб-приложения.
- Elasticsearch — хранилище данных, в котором лежит вся необходимая информация для сервса.
- Redis — хранилище данных для кэша.

## Используемые технологии
- FastAPI
- ElasticSearch
- Redis
- Docker
- Pytest + pytest coverage

## Запуск
1. Создать общую сеть для всех проектов практикума, чтобы была связь между всеми контейнерами курса
```shell
sudo docker network create yandex
```
2. Собрать и запустить проект ETL https://github.com/v-v-d/ETL
```shell
sudo docker-compose up --build
```
3. Очистить данные по последним выгрузкам:
```shell
sudo docker exec -it etl-redis redis-cli
```
и в командной оболочке выполнить очистку хранилища
```shell
127.0.0.1:6379> flushdb
```
4. Наполнить индексы эластика данными
```shell
sudo docker exec -it srv-etl python manage.py start-etl
```
5. Собрать и запустить текущий проект
```shell
sudo docker-compose up --build
```
6. Перейти к документации по адресу 0.0.0.0/api/docs. Дока закрыта бэйсик авторизацией.

## Тестирование
Собрать тестовое окружение и запустить тесты
```shell
sudo docker-compose -f docker-compose.test.yaml up --build
```
