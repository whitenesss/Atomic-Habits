from celery import Celery
from celery import shared_task
from django.db.models.signals import post_save, post_delete
from habits.models import Habit, HabitConnection
from django.dispatch import receiver
from habits.services import send_telegramm_massage, schedule_habit_tasks

app = Celery("config")


@shared_task
def send_inform(tg_name, message):
    print(tg_name, message)
    send_telegramm_massage(tg_name, message)


@receiver(post_save, sender=Habit)
def update_habit_schedule_post_save(sender, instance, **kwargs):
    schedule_habit_tasks()


@receiver(post_delete, sender=Habit)
def update_habit_schedule_post_delete(sender, instance, **kwargs):
    schedule_habit_tasks()


@receiver(post_save, sender=HabitConnection)
def update_habit_connection_schedule_post_save(sender, instance, **kwargs):
    schedule_habit_tasks()


@receiver(post_delete, sender=HabitConnection)
def update_habit_connection_schedule_post_delete(sender, instance, **kwargs):
    schedule_habit_tasks()


# Обновление расписания при загрузке приложения (например, при старте сервера)

schedule_habit_tasks()
