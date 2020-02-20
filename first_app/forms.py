from django import forms
from django.core import validators

class NameForm(forms.Form):
    name = forms.CharField(max_length=64)
    email = forms.EmailField()
    confirm_email = forms.EmailField(label="Confirm Email")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])    

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        confirm_email = all_clean_data['confirm_email']

        if(email != confirm_email):
            raise forms.ValidationError("Make Sure Email Matches.")
        