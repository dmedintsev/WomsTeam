from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    kat = models.CharField("Категория", max_length=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.kat


class Ticket(models.Model):
    user = models.ForeignKey(
        User, verbose_name="Пользователь", on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, verbose_name="Категория",
        on_delete=models.SET_NULL, null=True)
    tema = models.CharField("Тема", max_length=100)
    text = models.TextField("Текст", max_length=1000)
    created = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        ordering = ["category"]

    def __str__(self):
        return self.tema
