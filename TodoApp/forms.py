from django import forms
from django.contrib.auth import get_user_model

from .models import *


class TodoForm(forms.ModelForm):
    """ ToDOの入力フォーム
    """
    summary = forms.CharField(max_length=50, label="ToDo")
    detail = forms.CharField(max_length=100, label="詳細")
    limit = forms.DateField(label="期日")

    class Meta:
        model = Todo
        fields = '__all__'
