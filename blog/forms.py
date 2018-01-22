from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """Модель для отображения/редактирования комментариев
    """
    class Meta:
        model = Comment
        fields = ['user', 'text']
