from django.urls import path
from . import views

urlpatterns = [
    path('', views.startpage),
    path('singin', views.singin, name = 'singin')
]