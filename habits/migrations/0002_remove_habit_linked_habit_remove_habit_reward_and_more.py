# Generated by Django 5.0.7 on 2024-08-06 21:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="habit",
            name="linked_habit",
        ),
        migrations.RemoveField(
            model_name="habit",
            name="reward",
        ),
        migrations.CreateModel(
            name="HabitConnection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        help_text="Кусочек торта, Просмотр фильма",
                        max_length=200,
                        verbose_name="писание вознаграждения за выполнение полезной привычки",
                    ),
                ),
                (
                    "linked_habit",
                    models.ForeignKey(
                        blank=True,
                        help_text="Прогулка может быть связана с 'Чтением книги' как вознаграждение.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="habits.habit",
                        verbose_name="Ссылка на другую привычку, которая связана с текущей (только для полезных привычек)",
                    ),
                ),
            ],
            options={
                "verbose_name": "Связь привычек",
                "verbose_name_plural": "Связи привычек",
            },
        ),
    ]
