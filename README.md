# restaurant_booking

Веб-приложение для онлайн-бронирования столиков в ресторане.

## Функциональность

* регистрация и авторизация пользователей
* бронирование столиков
* управление бронированиями
* административная панель Django для управления данными
* асинхронная отправка email-уведомлений о бронировании (Celery)

## Технологии

* Python
* Django
* PostgreSQL
* Bootstrap
* Docker
* Celery (асинхронные задачи)
* Redis (брокер сообщений)

## Переменные окружения

Перед запуском проекта необходимо создать файл `.env` на основе `.env.sample`:

cp .env.sample .env

Для Windows:
copy .env.sample .env

или вручную скопировать и заполнить значения.

Пример переменных:

DATABASE_NAME=your_db
DATABASE_USER=your_user
DATABASE_PASSWORD=your_password
DATABASE_HOST=localhost
DATABASE_PORT=5432

EMAIL_BACKEND=...
EMAIL_HOST=...
EMAIL_HOST_USER=...

SECRET_KEY=your_secret_key

CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

## Асинхронные задачи

Для отправки email-уведомлений используется Celery.

После создания бронирования задача отправки письма выносится в отдельный процесс,
что позволяет не блокировать основной поток выполнения Django-приложения.

В качестве брокера сообщений используется Redis.

В режиме разработки используется console email backend - письма выводятся в терминал, 
что позволяет тестировать функциональность без настройки SMTP-сервера.

Для отправки email можно использовать SMTP (например, Yandex или Gmail).

В режиме разработки рекомендуется использовать:

EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend

## Запуск проекта

1. Клонировать репозиторий:

git clone <https://github.com/kseniya161-max/restaurant_booking>

2. Запустить контейнеры:

docker compose up --build

3. Открыть в браузере:

http://localhost:8000

4. В отдельном терминале запустить Celery worker:

poetry run celery -A config worker --loglevel=info --pool=solo

## Структура проекта

* `users` — приложение пользователей
* `booking` — логика бронирования
* `pages` — статические страницы сайта
