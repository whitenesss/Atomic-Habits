from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь", **NULLABLE
    )
    location = models.CharField(
        max_length=150,
        verbose_name="Место выполнения привычки",
        help_text="Пример: Дома, В парке",
    )
    start_date = models.TimeField(
        verbose_name="Дата начала",
        **NULLABLE,
        help_text="(формат 13:31) не обязательное поле",
    )
    action = models.CharField(
        max_length=200,
        verbose_name="Описание действия, составляющего привычку",
        help_text="Пример: Прогулка, Чтение",
    )
    is_pleasant = models.BooleanField(
        default=False,
        verbose_name="Указывает, является ли привычка приятной (вознаграждением)",
        help_text="True (если это приятная привычка), False (если это полезная привычка)",
    )
    linked_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Ссылка на другую привычку, которая связана с текущей (только для полезных привычек)",
        help_text="Прогулка может быть связана с 'Чтением книги' как вознаграждение.",
    )
    frequency = models.SmallIntegerField(
        verbose_name="Периодичность выполнения привычки в днях.",
        help_text="Пример: 1 (ежедневно), 7 (раз в неделю).",
    )

    reward = models.CharField(
        max_length=200,
        verbose_name="писание вознаграждения за выполнение полезной привычки",
        help_text="Кусочек торта, Просмотр фильма",
        **NULLABLE,
    )
    duration = models.SmallIntegerField(
        verbose_name="Предполагаемое время на выполнение привычки в секундах",
        help_text="Пример: 60 (максимальное значение — 120 секунд)",
    )
    is_public = models.BooleanField(
        default=False,
        verbose_name="Указывает на публичность привычки (может ли она быть видна другим пользователям)",
        help_text="True (публичная), False (частная)",
    )
    created_at = models.DateTimeField(
        **NULLABLE,
        verbose_name="Дата создания",
        help_text="Укажите дату создания",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        **NULLABLE,
        verbose_name="Дата изменения",
        help_text="Укажите дату изменения",
        auto_now=True,
    )

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"Я буду {self.action} в {self.start_date} в {self.location}"


class HabitConnection(models.Model):
    linked_habit = models.ForeignKey(
        Habit, on_delete=models.CASCADE,
        verbose_name="Ссылка на другую привычку, которая связана с текущей (только для полезных привычек)", **NULLABLE,
        help_text="Прогулка может быть связана с 'Чтением книги' как вознаграждение."
    )
    reward = models.CharField(
        max_length=200,
        verbose_name="писание вознаграждения за выполнение полезной привычки",
        help_text="Кусочек торта, Просмотр фильма",
    )

    class Meta:
        verbose_name = "Связь привычек"
        verbose_name_plural = "Связи привычек"

    def __str__(self):
        return f"{self.reward}"
