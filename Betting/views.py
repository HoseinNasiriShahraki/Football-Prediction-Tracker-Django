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


import matplotlib.pyplot as plt
from django.http import HttpResponse
from io import BytesIO

def plot_view(request):
    # Retrieve data
    Amin = Person.objects.get(name='Amin').history.split(',')
    Amin.pop()
    Mostafa = Person.objects.get(name='Mostafa').history.split(',')
    Mostafa.pop()
    Hosein = Person.objects.get(name='Hosein').history.split(',')
    Hosein.pop()
    Negar = Person.objects.get(name='Negar').history.split(',')
    Negar.pop()
    Tannaz = Person.objects.get(name='Tannaz').history.split(',')
    Tannaz.pop()
    Mohammad = Person.objects.get(name='Mohammad').history.split(',')
    Mohammad.pop()

    name_list = ['Amin', 'Mostafa', 'Hosein', 'Negar', 'Tannaz', 'Mohammad']
    lists = [Amin, Mostafa, Hosein, Negar, Tannaz, Mohammad]

    # Create plot
    plt.figure(figsize=(19, 10))
    for i, lst in enumerate(lists):
        plt.plot([int(x) for x in lst], label=name_list[i])
    
    plt.xlabel('Matches')
    plt.ylabel('Points')
    plt.title('Scores')
    plt.legend()
    plt.grid(True)

    # Save plot to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Create a HTTP response with the image
    return HttpResponse(buffer, content_type='image/png')


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
