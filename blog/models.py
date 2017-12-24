from django.db import models
from django.utils import timezone


class Category(models.Model):
    """ Класс модели категорий
    """
    cat = models.CharField("Категория", max_length=50)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.cat

class Tag(models.Model):
    """ Класс модели тегов
    """
    tag = models.CharField("Тег", max_length=50, unique=True)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.tag


class Post(models.Model):
    """ Класс модели поста
    """
    author = models.ForeignKey('auth.User', verbose_name="Автор", on_delete=models.CASCADE)
    title = models.CharField("Тема", max_length=100)
    mini_text = models.TextField("Краткое содержание", max_length=200)
    text = models.TextField("Содержание")
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    published_date = models.DateTimeField("Дата публикации", blank=True, null=True)
    image = models.ImageField("Изображение", upload_to="blog/", blank=True)
    category = models.ForeignKey(Category, verbose_name="Категория", blank=True, null=True, on_delete=models.SET_NULL)
    tag  = models.ManyToManyField(Tag, verbose_name="Тег", blank=True)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
