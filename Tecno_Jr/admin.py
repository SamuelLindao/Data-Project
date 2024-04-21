from django.contrib import admin

from .models import Tecno, SignIn


@admin.register(Tecno)
class TecnoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'url')


@admin.register(SignIn)
class SignInAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')