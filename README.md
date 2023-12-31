# Тестовое задание Softway
Данное приложение реализует REST API и предназначено для работы с задачами.
## Исползуемые технологии
  * python
  * django
  * django rest framework
  * drf-yasg
  * postgresql
  * cors
  * simple jwt
  * django-filters
## Сущности системы
  ### Задача
  * название
  * описание (опцонально)
  * статус
  * дата создания
  * пользователь
    
### Пользователь
* имя пользователя
* пароль
* почта (опционально)

## Документация API
Документация для API реализована с помощью drf-yasg и находится на следующем эндпоинте:
* http://127.0.0.1:8000/redoc/
## CORS
Для безопасности API реализован CORS с помощью django-cors-headers. 
В модуле ``settings.py`` необходимо внести изменения в следующие настройки, если у вас есть сторонние домены, обращающиеся к вашему API:
```
CORS_ALLOWED_ORIGINS = [
    "https://read-only.example.com",
    "https://read-and-write.example.com",
]
CSRF_TRUSTED_ORIGINS = [
    "https://read-and-write.example.com",
]
```

## JSON Web Token (JWT)
Авторизация на проекте реализована с помощью simple jwt токена, работа с которым находится на следующих эндпоинтах:
* http://127.0.0.1/token/
* http://127.0.0.1/token/refresh/

## Как использовать данный проект?
* Склонировать репозиторий в IDE и перейти в проект:

  В терминале ввести команды:
  ```
  git clone https://github.com/toir02/test-task-softway
  cd test-task-softway/
  ```
* Установить вирутальное окружение
  В терминале ввести команду:
  ```
  python3 -m venv venv
  ```
* Активировать виртуальное окружение
  В терминале ввести команду:
  ```
  source venv/bin/activate
  ```
* Установить зависимости
  В терминале ввести команду:
  ```
  pip install -r requirements.txt
  ```
* Создать файл ``.env``. Его необходимо заполнить данными из файла ``.env.sample``
* Создать базу данных, одноименную с названием базы данных в заполненном вами файле ``.env``
* Создать и применить миграции
  В терминале ввести следующие команды:
  ```
  python3 manage.py makemigrations
  ```
  ```
  python3 manage.py migrate
  ```
* Запустить сервер
  В терминале ввести команду:
  ```
  python3 manage.py runserver
  ```
## Контакты
Если у вас возникли вопросы или проблемы при использовании проекта, свяжитесь со мной.
tg: @toir02
