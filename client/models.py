from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """ Класс модели профиля пользователя
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # В поле birth_date null=True, так как при создании Пользователя и его
    # Профиля в раздельных формах (то есть, сначала Пользователя, потом его
    # Профиль, как, например, в немодифицированной еще Админке) модель User
    # отправит сигнал на создание строки Profile, а на этот момент значение
    # birth_date еще не известно.
    # Но blank=False (значение по умолчанию) позволит в формах обеспечить
    # обязательность заполнение пользователем этого поля.
    birth_date = models.DateField("Дата рождения", null=True,)

    # TODO: Уточнить путь для сохранения. Пока же указан upload_to="client/"
    avatar = models.ImageField("Аватар", upload_to="client/",
                               null=True, blank=True)

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили ползователей"

    def __str__(self):
        return self.user


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
