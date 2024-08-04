from django.db import models

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    user = models.ForeignKey()
    location = models.CharField(
        max_length=150,
        **NULLABLE,
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

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"Я буду {self.action} в {self.start_date} в {self.location}"
