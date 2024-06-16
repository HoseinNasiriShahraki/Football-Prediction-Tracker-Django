from cgitb import reset
from os import name
from re import Match
from tkinter import W
from turtle import title
from unittest import result
from django.shortcuts import render
from .models import Person, Match, Prediction, Team
from rest_framework.generics import RetrieveUpdateDestroyAPIView , ListAPIView , RetrieveUpdateAPIView, ListCreateAPIView
from .serializers import TeamSerializer, MatchSerializer, PersonSerializer, PredictionSerializer

def my_table_view(request):
    data = Person.objects.all()
    return render(request, 'my_table.html', {'data': data})


class PersonListAPIView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonAPIView(RetrieveUpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'name'

class MatchAPIView(ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class TeamAPIView(ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class PredictionAPIView(ListCreateAPIView):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer
