from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Person

class PersonINNSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'



