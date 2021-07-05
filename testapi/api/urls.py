from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.CreatePerson, name='CreatePerson'),
    path('show_all/', views.ShowAll, name='show'),
    path('people/<int:pk>/', views.SinglePerson, name='SinglePerson')
    
]
