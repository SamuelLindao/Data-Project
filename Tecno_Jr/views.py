from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as django_login
from django.contrib.auth.decorators import login_required
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Failed, that username is taken <3')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return render(request, 'login.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            django_login(request, user)

            return HttpResponse('Everything is good bro :3')
        else:
            return HttpResponse('Wrong username or password')

@login_required(login_url='/auth/login/')
def plat(request):
    return HttpResponse('Acessou!!')