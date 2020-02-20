from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('myform/', views.form_page, name="form_example"), 
]

