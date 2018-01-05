from django import forms
from django.contrib.auth.models import User
# from django.core.files.images import get_image_dimensions
from .models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birth_date', 'avatar',)
        localized_fields = ('birth_date',)
