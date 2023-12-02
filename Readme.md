# Проект Collection_of_Courses

Collection_of_Courses - проект онлайн-обучения, разработанный с использованием фреймворка Django.

## Технологии:

* python 3.11
* django 4.2.7
* djangorestframework 3.14.0
* django-celery-beat 2.5.0 
* django-cors-headers 4.3.1
* celery 5.3.5
* PostgreSQL
* psycopg2-binary 2.9.9
* pillow 10.1.0
* redis 5.0.1

## Установка:

Для установки и запуска проекта выполните следующие шаги:

1. Склонируйте репозиторий проекта на свой локальный компьютер git clone _https://github.com/SheenShaman/collection_of_courses_
2. Создайте виртуальное окружение _python3 -m venv мyenv_
3. Активируйте виртуальное окружение _myenv\Scripts\activate_
4. Установите зависимости _pip install -r requirements.txt_
5. Примените миграции _python manage.py migrate_
6. Запустите сервер разработки Django _python manage.py runserver_ 
7. Откройте приложение в вашем веб-браузере по адресу http://127.0.0.1:8000/

## Запуск проекта с помощью Docker:

Для запуска проекта через Docker необходимо:
1. Заполнить файл .env_sample
2. Выполнить команды:
- docker-compose build - сборка образа
- docker-compose up - запуск контейнера

Если БД не создана, то необходимо будет ее создать, но перед этим убедиться, что у вас запущен контейнер.
- Команда для создания БД: docker-compose exec db psql -U postgres

###### Автор проекта:

https://github.com/SheenShaman