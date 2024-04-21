from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_now=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Tecno(Base):
    nome = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Tecno'
        verbose_name_plural = 'Tecnos'

    def __str__(self):
        return self.nome


class SignIn(Base):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return {self.username, self.password}