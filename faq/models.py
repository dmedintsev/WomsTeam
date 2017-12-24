from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Faq(models.Model):
    """ Класс модели FAQ
    """
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE)
    title = models.CharField("Вопрос", max_length=100)
    opisanie = models.TextField("Описание", max_length=1000)
    date = models.DateField("Создан", auto_now_add=True)

    class Meta:
        verbose_name = "Вопрос\Ответ"
        verbose_name_plural = "Вопросы\Ответы"
        ordering = ["title"]

    def __str__(self):
        return self.title
