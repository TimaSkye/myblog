from .models import Users
from django.forms import ModelForm, TextInput


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['user_name', 'location']

        widgets = {
            'user_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Ваше имя'
            }),
            'location': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Откуда Вы?'
            })
        }