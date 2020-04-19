from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from . import forms

# Create your views here.

def index(request):
    return render(request, 'first_app/index.html', context=None)

def register(request):
    if(request.method == 'POST'):
        form = forms.RegisterForm(request.POST)
        if(form.is_valid()):
            form.save()
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password')
            password2 = form.cleaned_data.get('confirm_password')
            print(password1, password2)
            if(password1 == password2):
                account = authenticate(email=email, password=password1)
                login(request, account)
                return redirect('index')
            else:
                raise ValueError('Both passwords should match')
        else:
            form = form
    else:
        form = forms.RegisterForm()
    
    print(form)
    return render(request, 'first_app/register.html', {'form':form})