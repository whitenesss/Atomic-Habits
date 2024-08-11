from rest_framework.serializers import ValidationError


class FrequencyValidator:
    def __init__(self, fielf):
        self.fielf = fielf

    def __call__(self, value):
        if value["frequency"] <= 0 or value["frequency"] >= 8:
            raise ValidationError(
                f"Периодичность выполнения привычки в днях не должно быть меньше 1 и больше 7"
            )


class DurationValidator:
    def __init__(self, fielf):
        self.fielf = fielf

    def __call__(self, value):
        if value["duration"] <= 0 or value["duration"] >= 120:
            raise ValidationError(
                f"Предполагаемое время на выполнение привычки в секундах не должно быть меньше 0 или больше 120"
            )
