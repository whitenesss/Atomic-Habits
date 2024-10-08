# Generated by Django 5.0.7 on 2024-08-06 22:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0002_remove_habit_linked_habit_remove_habit_reward_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="habit",
            name="linked_habit",
            field=models.ForeignKey(
                blank=True,
                help_text="Прогулка может быть связана с 'Чтением книги' как вознаграждение.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="habits.habit",
                verbose_name="Ссылка на другую привычку, которая связана с текущей (только для полезных привычек)",
            ),
        ),
        migrations.AddField(
            model_name="habit",
            name="reward",
            field=models.CharField(
                blank=True,
                help_text="Кусочек торта, Просмотр фильма",
                max_length=200,
                null=True,
                verbose_name="писание вознаграждения за выполнение полезной привычки",
            ),
        ),
    ]
