# Проект DRF postapi

Этот проект представляет собой API для управления постами в блоге. Он разработан с использованием Django и Django REST
Framework.

## Установка

1. Клонируйте репозиторий на локальную машину:

   ```console
   git clone https://github.com/KolyanLock/postapi.git
   ```

2. Перейдите в директорию проекта:

   ```console
   cd postapi
   ```

3. Создайте виртуальную среду и активируйте ее:

   Для Windows:

   ```cmd
   python -m venv .venv
   .venv\Scripts\activate
   ```

   Для Linux/Mac:

   ```bush
   python3 -m venv .venv
   source .venv/bin/activate
   ```
   Примечание: В Linux вы можете использовать python вместо python3, в зависимости от конфигурации вашей системы.

4. Установите зависимости:

   ```console
   pip install -r requirements.txt
   ```

5. Настройте базу данных в файле settings.py:

   ```code
   DATABASES = {
    'default': {
        'ENGINE': '<драйвер базы данных>',
        'NAME': '<имя базы данных>',
        'USER': '<пользователь>',
        'PASSWORD': '<пароль>',
        'HOST': '<хост>',
        'PORT': '<порт>',
     }
   }
   ```

6. Примените миграции:

   ```console
   python manage.py migrate
   ```

7. Запустите сервер разработки:

    ```console
   phpCopy code
   python manage.py runserver <хост>:<порт>
   ```
   Теперь API должно быть доступно по указанному хосту и порту.

## Endpoints

**GET /api/posts/**

Возвращает список всех постов

Пример запроса:

```
GET /api/posts/ HTTP/1.1
Host: <хост>:<порт>
```

**POST /api/posts/**

Создает новый пост. Требуется аутентификация с использованием токена пользователя.

Пример запроса:

```
POST /api/posts/ HTTP/1.1
Host: <хост>:<порт>
Authorization: Token <токен пользователя>
Content-Type: application/json
```
```
{
  "title": "Заголовок поста",
  "slug": "url-поста",
  "content": "Содержимое поста",
  "category": <id категории>,
  "tags": [<список id тегов>]
}
```

**GET /api/posts/{slug}/**

Возвращает информацию о конкретном посте.

Пример запроса:

```
GET /api/posts/{slug}/ HTTP/1.1
Host: <хост>:<порт>
```

PUT /api/posts/{slug}/

Обновляет информацию о конкретном посте. Требуется аутентификация с использованием токена пользователя.

Пример запроса:

```
GET /api/posts/{slug}/ HTTP/1.1
Host: <хост>:<порт>
```

**DELETE /api/posts/{slug}/**

Удаляет конкретный пост. Требуется аутентификация с использованием токена пользователя.

Пример запроса:

```
DELETE /api/posts/{slug}/ HTTP/1.1
Host: <хост>:<порт>
Authorization: Token <токен пользователя>
```

## Аутентификация

API поддерживает следующие методы аутентификации:
   - Token Authentication: Для аутентификации пользователя используется токен, который можно получить через /auth/token/login/
   - Basic Authentication: Аутентификация с использованием базовых авторизационных данных (логин и пароль) через auth/basic/login/
   - Session Authentication: Аутентификация с использованием сессий auth/basic/login/

## Пагинация

API использует пагинацию по умолчанию с лимитом отображения 10 записей на странице.

## Фильтрация

API поддерживает фильтрацию с использованием DjangoFilterBackend. Вы можете фильтровать посты по полям категроий и тегов, передавая параметр в URL запроса.

Пример URL для фильтрации постов по категории:

```
/api/posts/?category=<slug категории>
```
```
/api/posts/?teg=<slug тега>
```
