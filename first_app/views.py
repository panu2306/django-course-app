from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.

def index(request):
    return render(request, 'first_app/index.html', context=None)

def form_page(request):
    form = forms.NameForm()
    if(request.method == 'POST'):
        form = forms.NameForm(request.POST)

        if(form.is_valid()):
            print("Validation Successful!!!")
            print("Name:" + form.cleaned_data['name'])
            print("Email:" + form.cleaned_data['email'])
            print("Text:" + form.cleaned_data['text'])
    return render(request, 'first_app/form_page.html', context={'form': form})
