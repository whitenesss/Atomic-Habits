# Atomic-Habits

**Atomic-Habits** — это трекер полезных привычек, который поможет вам формировать и поддерживать новые привычки. Вы будете получать уведомления о выполнении привычек прямо в Telegram.

## Технологии

- **Python**
- **Django**
- **Django REST Framework (DRF)**
- **PostgreSQL**
- **Redis**
- **Celery**

## Установка и настройка

1. **Клонируйте репозиторий**
    Клонируйте репозиторий на свой компьютер с использованием SSH ключа:
    git clone <ваш_репозиторий_SSH_URL>

2. **Установите зависимости**
    Установите все необходимые зависимости из requirements.txt:
    pip install -r requirements.txt

3. **Настройте переменные окружения**
    Создайте файл .env и внесите свои данные. Необходимые переменные перечислены в файле .env.sample.

4. **Выполните команды для создания и применения миграций**
    python manage.py makemigrations
    python manage.py migrate

5. **Установите и запустите Redis**
    Установите Redis и запустите его командой:
    redis-server

6. **Запустите сервер Django**
    Запустите сервер Django командой:
    python manage.py runserver

7. **Настройте Celery**
    в терминале запустите celery worker командой: celery -A config worker -l INFO # для Mac и Linux celery -A config worker -l INFO -P eventlet # для Windows
    в другом терминале запустите celery beat командой: celery -A config beat -l info -S django



  **Регистрация и создание привычек**

Зарегистрируйтесь в программе Postman и создайте привычки, отправив POST запрос с телом JSON:
{
    "location":"улица", :Локация выполнения привычки
    "start_date":"01:55",:Выремя оповещения о привычки 
    "action":"бег",: Действия, составляющего привычку 
    "is_pleasant":"False",: Указывает, является ли привычка приятной (вознаграждением)
    "linked_habit": id: "Ссылка на другую привычку, которая связана с текущей (только для полезных привычек)"
    "frequency":"2",: преодичность выполнения привычки где 
        1-понедельник; 
        2-понедельник, среда; 
        3-понедельник, среда , пятница; 
        4-понедельник, среда ,пятница , воскресенье; 
        5-понедельник, вторник, среда, четверк, пятница;
        6-понедельник, вторник, среда ,четверк, пятница, суббота;
        7-понедельник, вторник, среда , четверк, пятница, суббота, воскресенье;
    "duration":"60",: Предполагаемое время на выполнение привычки в секундах
    "is_public":"False",: Указывает на публичность привычки (может ли она быть видна другим пользователям)
    "reward":"Просмотр фильма": Описание вознаграждения за выполнение полезной привычки
}

    **зайдите в телеграм бот и нажмите START**





Зайдите в Telegram бот и нажмите START.
