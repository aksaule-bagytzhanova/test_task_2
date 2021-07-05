from django.db.models import fields
from django.db.models.query_utils import FilteredRelation
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Person
from datetime import date

class PersonINNSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['iin']

class ResultIINSerilizer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField('get_age')
    today = date.today()
    
    def get_age(self, geta):
        iina = getattr(geta, "iin")
        if iina
        return int(iina)

    class Meta:
        model = Person
        fields = ['iin', 'age']



