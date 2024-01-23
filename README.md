# Как развернуть проект

1. Склонируйте проект командой: git clone https://github.com/aiafaa/dollar-rate.git

2. Создайте виртуальное окружение: `python -m venv venv`

4. Активируйте окружение: `venv/Scripts/activate`

5. Установите зависимости: `pip install -r requirements.txt`

6. Создайте миграцию: `python manage.py makemigrations` `python manage.py migrate`

8. Запустите проект командой - `python manage.py runserver`

10. Перейдите по ссылке http://127.0.0.1:8000/get-current-usd/
