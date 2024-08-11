Atomic-Habits
Atomic-Habits — это трекер полезных привычек, который поможет вам формировать и поддерживать новые привычки. Вы будете получать уведомления о выполнении привычек прямо в Telegram.

Технологии
Python
Django
Django REST Framework (DRF)
PostgreSQL
Redis
Celery
Установка и настройка
Клонирование репозитория:

Клонируйте репозиторий на свой компьютер с использованием SSH ключа:

bash
Копировать код
git clone <ваш_репозиторий_SSH_URL>
Установка зависимостей:

Установите все необходимые зависимости из requirements.txt:

bash
Копировать код
pip install -r requirements.txt
Настройка переменных окружения:

Создайте файл .env и внесите свои данные. Необходимые переменные перечислены в файле .env.sample.

Создание и применение миграций:

Выполните команды для создания и применения миграций:

bash
Копировать код
python manage.py makemigrations
python manage.py migrate
Установка и запуск Redis:

Установите Redis и запустите его командой:

bash
Копировать код
redis-server
Запуск проекта:

Запустите сервер Django:

bash
Копировать код
python manage.py runserver
Настройка Celery:

В одном терминале запустите Celery worker:

bash
Копировать код
celery -A config worker -l INFO
Для Mac и Linux:

bash
Копировать код
celery -A config worker -l INFO
Для Windows:

bash
Копировать код
celery -A config worker -l INFO -P eventlet
В другом терминале запустите Celery beat:

bash
Копировать код
celery -A config beat -l info -S django
Регистрация и создание привычек:

Зарегистрируйтесь в программе Postman и создайте привычки, отправив POST запрос с телом JSON:

json
Копировать код
{
    "location": "улица", 
    "start_date": "01:55", 
    "action": "бег", 
    "is_pleasant": "False",
    "linked_habit": "id", 
    "frequency": "2", 
    "duration": "60", 
    "is_public": "False", 
    "reward": "Просмотр фильма"
}
location: Локация выполнения привычки
start_date: Время оповещения о привычке
action: Действие, составляющее привычку
is_pleasant: Указывает, является ли привычка приятной (вознаграждением)
linked_habit: Ссылка на другую привычку, которая связана с текущей (только для полезных привычек)
frequency: Частота выполнения привычки (1-понедельник, 2-понедельник и среда, и т.д.)
duration: Предполагаемое время на выполнение привычки в секундах
is_public: Указывает на публичность привычки (может ли она быть видна другим пользователям)
reward: Описание вознаграждения за выполнение полезной привычки
Запуск Telegram бота:

Зайдите в Telegram бот и нажмите START.
