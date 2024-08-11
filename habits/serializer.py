from rest_framework import serializers

from habits.models import Habit, HabitConnection
from habits.validators import FrequencyValidator, DurationValidator


class UserHabit(serializers.ModelSerializer):
    class Meta:
        model = HabitConnection
        fields = ["habit"]


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"


class HabitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            FrequencyValidator(fielf="frequency"),
            DurationValidator(fielf="duration"),
        ]

    def validate(self, data):
        print("Validating data:", data)
        """проверяем ввод данных пользовалетеля по положительным и связанным привычкам"""
        if data.get("reward") and data.get("linked_habit"):
            raise serializers.ValidationError(
                "может быть либо вознограждение либо связанная привычка"
            )

        if data.get("is_pleasant"):
            print("privet")
            if data.get("linked_habit") or data.get("reward"):
                raise serializers.ValidationError(
                    "положительная привычка не должна быть со связанной привычкой или вознограждением"
                )

        if data.get("linked_habit") and (not data.get("linked_habit").is_pleasant):
            raise serializers.ValidationError(
                "связанная привычка должна быть положительной"
            )
        return data


class HabitListSerializer(serializers.ModelSerializer):
    # habit_public = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Habit
        fields = [
            "id",
            "location",
            "start_date",
            "action",
            "linked_habit",
            "frequency",
            "reward",
            "duration",
            "is_public",
        ]

    # def get_habit_public(self, obj):
    #     print(obj)
    #     user = self.context['request'].user
    #     return HabitConnection.objects.filter(user=user, habit=obj)
