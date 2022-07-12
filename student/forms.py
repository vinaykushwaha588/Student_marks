from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Mark

class MarksModelForm(forms.ModelForm):
    class Meta:
        model  = Mark
        fields ="__all__"