# CSVReader Backend

## Требования
 - Python 3.10
 - Redis
 - SQLite

## Настройка проекта

### 1. Установка зависимостей
```sh
pip install -r requirements.txt
```

### 2. Настройка файла окружения
```sh
nano .env
```
(переменные см. в файле .env-sample)

```sh
pip install python-dotenv[cli]
```

### 3. Проведение миграций
```sh
dotenv -f .env run ./manage.py migrate
```

### Запуск сервера для разработки

```sh
dotenv -f .env run ./manage.py runserver
```

### Запуск Celery(нужен Redis Server)

```sh
dotenv -f .env run celery -A csvreader worker -l INFO
```
