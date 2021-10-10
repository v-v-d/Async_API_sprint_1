## Запуск
1. Создать общую сеть для всех проектов практикума, чтобы была связь между всеми контейнерами курса
```shell
sudo docker network create yandex
```
2. Собрать и запустить проект ETL https://github.com/v-v-d/ETL
```shell
sudo docker-compose up --build
```
3. Очистить данные по последним выгрузкам
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
6. Перейти к документации по адресу 0.0.0.0:8088/api/docs