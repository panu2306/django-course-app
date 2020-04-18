from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data('email')
        qs = User.objects.filter(email=email)
        if(qs.exists()):
            raise forms.ValidationError('Email is taken already.')
        return email
    
    def clean_password(self):
        password = self.cleaned_data('password')
        password2 = self.cleaned_data('password2')

        if(password and password2 and password != password2):
            raise forms.ValidationError('Passwords do not match')
        
        return password2

class UserAdminCreationForm(forms.ModelForm):
    """
        A form for creating new users. Includes all the required
        fields, plus a repeated password.
    """

    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'full_name']

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']

        if(password and password2 and password != password2):
            raise forms.ValidationError('Passwords do not match')

        return password2
    
    def save(self, commit=True):
        # save the provided password in hash format 
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'full_name', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]