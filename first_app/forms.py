from django import forms
from django.core import validators

class NameForm(forms.Form):
    name = forms.CharField(max_length=64)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])    