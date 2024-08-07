from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email address")
    phone_number = models.CharField(
        max_length=35, verbose_name="Phone number", blank=True, null=True
    )
    tg_name = models.CharField(
        max_length=50, verbose_name="Telegram username", blank=True, null=True
    )
    avatar = models.ImageField(
        upload_to="users/avatars", verbose_name="Avatar", blank=True, null=True
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return f"Email: {self.email} Tg name: {self.tg_name}"
