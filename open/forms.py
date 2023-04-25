from .models import Articles

from django import forms

class ArticlesForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)

