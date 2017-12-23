# -*- coding: utf-8 -*-
from django import forms
from .models import Ticket


class FormTicket(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["category", "tema", "text"]
