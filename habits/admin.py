from django.contrib import admin

from habits.models import Habit, HabitConnection


# Register your models here.
@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "owner",
        "location",
        "start_date",
        "action",
        "is_pleasant",

        "frequency",

        "duration",
        "is_public",
        "created_at",
        "updated_at",
    )


# @admin.register(HabitConnection)
# class HabitConnectionAdmin(admin.ModelAdmin):
#     list_display = ("id", "linked_habit", "reward")
