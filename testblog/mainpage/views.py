from django.shortcuts import render
from .models import Callback
from .forms import CallbackForm


def mainpage(request):
    error = ''
    if request.method == "POST":
        form = CallbackForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "Некорректно заполнена форма!"

    form = CallbackForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'mainpage/content.html', data)


def bio(request):
    error = ''
    if request.method == "POST":
        form = CallbackForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "Некорректно заполнена форма!"

    form = CallbackForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'mainpage/bio.html', data)


def pydjango(request):
    error = ''
    if request.method == "POST":
        form = CallbackForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "Некорректно заполнена форма!"

    form = CallbackForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'mainpage/pydjango.html', data)


def pykivy(request):
    error = ''
    if request.method == "POST":
        form = CallbackForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "Некорректно заполнена форма!"

    form = CallbackForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'mainpage/pykivy.html', data)


def pybots(request):
    error = ''
    if request.method == "POST":
        form = CallbackForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "Некорректно заполнена форма!"

    form = CallbackForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'mainpage/pybots.html', data)


def nocode(request):
    error = ''
    if request.method == "POST":
        form = CallbackForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "Некорректно заполнена форма!"

    form = CallbackForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'mainpage/nocode.html', data)


def content(request):
    error = ''
    if request.method == "POST":
        form = CallbackForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "Некорректно заполнена форма!"

    form = CallbackForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'mainpage/content.html', data)
