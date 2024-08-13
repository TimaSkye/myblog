from .models import Callback
from django.forms import ModelForm, TextInput, EmailInput, Textarea


class CallbackForm(ModelForm):
    class Meta:
        model = Callback
        fields = ['user_name', 'phone_num', 'email', 'text_inform']

        widgets = {
            "user_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            "phone_num": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш номер телефона'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш email'
            }),
            "text_inform": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите сопроводительное сообщение'
            })
        }
