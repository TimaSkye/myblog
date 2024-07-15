from django.shortcuts import render

def mainpage(request):
    return render(request, 'mainpage/content.html')

def bio(request):
    return render(request, 'mainpage/bio.html')

def pydjango(request):
    return render(request, 'mainpage/pydjango.html')

def pykivy(request):
    return render(request, 'mainpage/pykivy.html')

def pybots(request):
    return render(request, 'mainpage/pybots.html')

def nocode(request):
    return render(request, 'mainpage/nocode.html')

def content(request):
    return render(request, 'mainpage/content.html')

def callback(request):
    return render(request, 'mainpage/callback.html')