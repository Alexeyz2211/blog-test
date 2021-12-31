# blog-test
Для запуска проекта сначала нужно провести миграции прописав в терминал комманды python manage.py makemigrations, python manage.py migrate.
Затем для того что бы работала отправка сообщений в blog/setting.py в поля EMAIL_HOST_USER нужно вписать электронный адрес отправителя а в EMAIL_HOST_PASSWORD подходящий пароль.
Затем прописать docker-compose up --build и все поедет.
