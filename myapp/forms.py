from django import forms
from .models import TodoItem


class MyForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = '__all__'
