from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """ Класс модели категорий курсов
    """
    title = models.CharField("Заголовок", max_length=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Course(models.Model):
    """ Класс модели курсов
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="Категория",
                                 on_delete=models.SET_NULL, blank=True,
                                 null=True)
    title = models.CharField("Заголовок", max_length=100, )
    price = models.IntegerField("Цена", blank=True, null=True,)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title


class Task(models.Model):
    """ Класс модели заданий для курсов
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    сourse = models.ForeignKey(Course, verbose_name="Курс",
                               on_delete=models.SET_NULL, blank=True,
                               null=True,)
    title = models.CharField("Заголовок", max_length=100, )
    text = models.TextField("Текст (теория) с примерами", max_length=5000)
    code = models.TextField("Тест задание", max_length=5000)
    correct_answer = models.TextField("Верный ответ", max_length=5000)
    answer = models.TextField("Ответ пользователя", max_length=5000)

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"

    def __str__(self):
        return self.title
