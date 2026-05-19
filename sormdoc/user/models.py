from django.db import models
from django.conf import settings


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    telegram_id = models.BigIntegerField(
        unique=True,
        null=True,
        blank=True,
        help_text="ID пользователя в Telegram (целое число).",
    )
    phone = models.CharField(
        max_length=32,
        blank=True,
        help_text="Контактный телефон (в произвольном формате или E.164).",
    )

    patronymic = models.CharField("Отчество", max_length=150, blank=True)

    @property
    def first_name(self) -> str:
        return self.user.first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        self.user.first_name = value

    @property
    def last_name(self) -> str:
        return self.user.last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        self.user.last_name = value

    def save(self, *args, **kwargs):
        # Если вы присваивали profile.first_name/last_name, изменения лежат в self.user
        # — сохраним пользователя перед сохранением профиля.
        if self.user_id is not None:
            self.user.save(update_fields=["first_name", "last_name"])
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Profile({self.user!s})"

    #Сюда можно добавлять параметры профиля пользователя