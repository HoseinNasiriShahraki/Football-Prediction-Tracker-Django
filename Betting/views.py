from django.shortcuts import render
from .models import Person, Match, Prediction, Team
from rest_framework.generics import UpdateAPIView , ListAPIView , ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .serializers import TeamSerializer, MatchSerializer, PersonSerializer, PredictionSerializer
from .models import calculate_points

calculate_points()

def my_table_view(request):
    calculate_points()
    data = Person.objects.all()
    return render(request, 'my_table.html', {'data': data})


class PersonListAPIView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'name'

class MatchAPIView(ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    filterset_fields = ['status']

class MatchUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    filterset_fields = ['status']

class TeamAPIView(ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class PredictionAPIView(ListCreateAPIView):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer
    filterset_fields = ['person']
