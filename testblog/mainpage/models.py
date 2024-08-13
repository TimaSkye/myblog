from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


class Callback(models.Model):
    user_name = models.CharField('Имя', max_length=50)
    phone_num = PhoneNumberField('Номер телефона', blank=False)
    email = models.EmailField('Email', max_length=75)
    text_inform = models.CharField('Сообщение', max_length=350)
    date = models.DateTimeField('Дата регистрации', default=timezone.now)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"
