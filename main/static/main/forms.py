from django import forms

class MyForm(forms.Form):
    my_field = forms.CharField(label='My Label', max_length=100)

