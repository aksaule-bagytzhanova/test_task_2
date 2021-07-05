from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from rest_framework import status
from .serializers import PersonINNSerilizer, ResultIINSerilizer
from .models import Person
# Create your views here.


@api_view(['GET'])
def ShowAll(request):
    person = Person.objects.all()
    serializer = PersonINNSerilizer(person, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def SinglePerson(request, pk):
    person = Person.objects.get(iin=pk)
    serializer = ResultIINSerilizer(person, many=False)
    return Response(serializer.data)

@api_view(["POST"])
def CreatePerson(request):
    serializer = PersonINNSerilizer(data=request.data)

    if serializer.is_valid():
        iin_in = request.data.get("iin")
        print(iin_in)
        serializer.save()
    
    return Response(serializer.data)

