from django.db import models
from django.utils import timezone


class Users(models.Model):
    user_name = models.CharField('Имя', max_length=50)
    location = models.CharField('Локация', max_length=50)
    date = models.DateTimeField('Дата регистрации', default=timezone.now)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"