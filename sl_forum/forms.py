from django import forms
from .models import TopicForum, MessageForum, UserForum


class TopicForm(forms.ModelForm):
    """Создание темы на форуме"""
    class Meta:
        model = TopicForum
        exclude = ('user',)


class MessageForm(forms.ModelForm):
    """Создание сообщения на форуме"""
    class Meta:
        model = MessageForum
        exclude = ('user', 'topic')


class UserForumForm(forms.ModelForm):
    """Создание профиля пользователя на форуме"""
    class Meta:
        model = UserForum
        fields = ('name', 'views')
