from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('push-iin', views.Pushiin, name='push-iin'),
    path('get-age', views.Getiin, name='get-iin')
]
