from django.shortcuts import render, redirect
from .models import Users
from .forms import UsersForm


def startpage(request):
    return render(request, 'welcomepage/welcome.html')

def singin(request):
    error = ''
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mainpage/')
        else:
            error = 'Некоректное заполнение формы'
    form = UsersForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'welcomepage/login.html', data)