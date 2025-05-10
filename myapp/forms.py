from django import forms


class MyForm(forms.ModelForm):
    todo = forms.CharField(label="To do", max_length=100)