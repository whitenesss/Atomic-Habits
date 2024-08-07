from rest_framework import serializers

from habits.models import Habit


# class HabitConnectionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HabitConnection
#         fields = ["id", "linked_habit", "reward"]


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"


class HabitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, data):
        print("Validating data:", data)
        # print(data.get('reward'))
        """проверяем ввод данных пользовалетеля по положительным и связанным привычкам"""
        if data.get('reward') and data.get('linked_habit'):
            raise serializers.ValidationError('может быть либо вознограждение либо связанная привычка')

        if data.get('is_pleasant'):
            print('privet')
            if data.get('linked_habit') or data.get('reward'):
                raise serializers.ValidationError(
                    'положительная привычка не должна быть со связанной привычкой или вознограждением')

        if data.get('linked_habit') and (not data.get('linked_habit').is_pleasant):
            raise serializers.ValidationError(
                'связанная привычка должна быть положительной')
        return data
