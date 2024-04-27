from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('plat/', views.plat, name='plat')

]

