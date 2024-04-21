from django.shortcuts import render


def home(request):
    print(request.headers)
    return render(request, 'home.html')
