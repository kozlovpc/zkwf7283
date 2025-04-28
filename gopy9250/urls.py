from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dynamic_form, name='form'),
    path('success/', views.success_view, name='success'),
    path('save-data/', views.save_data, name='save_data'),
    ]