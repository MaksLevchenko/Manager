from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Client(models.Model):
    """Модель клиента"""
    name = models.CharField(max_length=30, verbose_name='Имя')
    lastName = models.CharField(max_length=30, verbose_name='Фамилия')
    phone = models.PositiveSmallIntegerField(verbose_name='Телефон')
    email = models.EmailField()

    def get_absolute_url(self):
        return reverse("client_detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Comment(models.Model):
    """Модель комментария"""
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name')
    text = models.TextField()

    class Meta:
        ordering = ['-id']
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.text
