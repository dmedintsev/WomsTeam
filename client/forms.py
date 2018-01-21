from django import forms
from django.contrib.auth.models import User
# from django.core.files.images import get_image_dimensions
from .models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name':forms.TextInput(attrs={'placeholder':'Имя'}),
            'last_name': forms.TextInput(attrs={'placeholder':'Фамилия'}),
            'email': forms.TextInput(attrs={'placeholder':'Эл. почта'})
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birth_date', 'avatar',)
        localized_fields = ('birth_date',)
        widgets = {
            'birth_date':forms.TextInput(attrs={'placeholder':'Дата рождения'}),
        }
