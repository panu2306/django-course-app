from django import forms

class NameForm(forms.Form):
    name = forms.CharField(max_length=64)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    