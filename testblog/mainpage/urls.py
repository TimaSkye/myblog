from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name="index"),
    path('content/', views.mainpage, name="content"),
    path('bio/', views.bio, name="bio"),
    path('pydjango/', views.pydjango, name="pydjango"),
    path('pykivy/', views.pykivy, name="pykivy"),
    path('pybots/', views.pybots, name="pybots"),
    path('nocode/', views.nocode, name="nocode"),
    path('callback/', views.callback, name="callback"),
]