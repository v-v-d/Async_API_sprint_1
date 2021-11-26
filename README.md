![tests](https://github.com/v-v-d/Async_API_sprint_1/actions/workflows/tests.yml/badge.svg)
[![codecov](https://codecov.io/gh/v-v-d/Async_API_sprint_1/branch/main/graph/badge.svg?token=Q8NOGB813N)](https://codecov.io/gh/v-v-d/Async_API_sprint_1)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

# API для кинотеатра

Точка входа для всех клиентов.

## Ресурсы
- Доска: https://github.com/users/v-v-d/projects/3

Репозитории:
- сервис Auth API: https://github.com/v-v-d/Auth_sprint_1
- сервис API: https://github.com/v-v-d/Async_API_sprint_1
- сервис ETL: https://github.com/v-v-d/ETL
- сервис Admin panel: https://github.com/v-v-d/Admin_panel_sprint_1


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
docker network create yandex
```
2. Собрать и запустить проект ETL https://github.com/v-v-d/ETL
```shell
docker-compose up --build
```
3. Очистить данные по последним выгрузкам:
```shell
docker exec -it etl-redis redis-cli
```
и в командной оболочке выполнить очистку хранилища
```shell
127.0.0.1:6379> flushdb
```
4. Наполнить индексы эластика данными
```shell
docker exec -it srv-etl python manage.py start-etl
```
5. Собрать и запустить текущий проект
```shell
docker-compose up --build
```
6. Перейти к документации по адресу 0.0.0.0/api/docs. Дока закрыта бэйсик авторизацией.

## Тестирование
Собрать тестовое окружение и запустить тесты
```shell
docker-compose -f docker-compose.test.yaml up --build
```
