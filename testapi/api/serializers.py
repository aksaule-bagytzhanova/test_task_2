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
    global year 
    global month
    global day
    year = today.year
    month = today.month
    day = today.day
    def get_age(self, geta):
        iina = getattr(geta, "iin")
        if int(iina[0:2])>=21:
            if int(iina[2:4])>= month:
                if int(iina[4:6])>= day:
                    return year - (+int(iina[0:2]))
                else:
                    return year - (1898+int(iina[0:2]))
            else:
                return year - (1899+int(iina[0:2]))
        else:
            if int(iina[2:4])>= month:
                return year - (2000+int(iina[0:2]))
            else:
                return year - (1999+int(iina[0:2]))


    class Meta:
        model = Person
        fields = ['iin', 'age']



