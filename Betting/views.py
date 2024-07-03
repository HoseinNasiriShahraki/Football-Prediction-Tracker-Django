from django.shortcuts import render
from .models import Person, Match, Prediction, Team
from rest_framework import filters
from rest_framework.generics import UpdateAPIView , ListAPIView , ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .serializers import TeamSerializer, MatchSerializer, PersonSerializer, PredictionSerializer
from .models import calculate_points
from .tables import MyTable

calculate_points()

def my_table_view(request):
    calculate_points()
    table = MyTable(Person.objects.all())
    return render(request, 'my_table.html', {'table': table})


def standardize_pairs(input_list):
    output_list = []
    for pair in input_list:
        sorted_pair = sorted(pair)
        output_list.append(sorted_pair)
    return output_list


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
    
    # Adjust the grid
    plt.grid(which='both', axis='both', linestyle='-', linewidth=0.5)

    # Set the major ticks
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))
    plt.gca().yaxis.set_major_locator(plt.MultipleLocator(5))

    # Save plot to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Create an HTTP response with the image
    return HttpResponse(buffer, content_type='image/png')


def plot_view2(request):
    from collections import defaultdict

    def create_list(person):
        l1 = []
        for pred in person:
            l1.append([pred.Team_1_pred, pred.Team_2_pred])
        l1 = standardize_pairs(l1)
        return l1
    
    Amin = Prediction.objects.filter(persons_name='Amin')
    Amin_pred_list = create_list(Amin)
    
    Mostafa = Prediction.objects.filter(persons_name='Mostafa')
    Mostafa_pred_list = create_list(Mostafa)

    Hosein = Prediction.objects.filter(persons_name="Hosein")
    Hosein_pred_list = create_list(Hosein)

    Negar = Prediction.objects.filter(persons_name='Negar')
    Negar_pred_list = create_list(Negar)

    Tannaz = Prediction.objects.filter(persons_name='Tannaz')
    Tannaz_pred_list = create_list(Tannaz)

    Mohammad = Prediction.objects.filter(persons_name="Mohammad")
    Mohammad_pred_list = create_list(Mohammad)

    pred_list = [Amin_pred_list, Mostafa_pred_list, Hosein_pred_list, Negar_pred_list, Tannaz_pred_list, Mohammad_pred_list]
    labels = ["Amin", "Mostafa", "Hosein", "Negar", "Tannaz", "Mohammad"]

        
    # Step 2: Count occurrences of each coordinate
    def draw(pr_list):  
        fig, axes = plt.subplots(3, 2, figsize=(12, 12))  # 3 rows, 2 columns
        axes = axes.flatten()  # Flatten the 2D array of axes to 1D for easier iteration

        # Step 3: Plot each list of coordinates in its own subplot
        for i, coords in enumerate(pr_list):
        # Count occurrences of each coordinate
            coord_counts = defaultdict(int)
            for coord in coords:
                coord_counts[tuple(coord)] += 1

            x_vals = [pair[0] for pair in coords]
            y_vals = [pair[1] for pair in coords]

            sizes = [coord_counts[tuple(coord)] * 80 for coord in coords]  # Adjust size multiplier as needed

            axes[i].scatter(x_vals, y_vals, s=sizes, alpha=0.5, c='green')
            axes[i].set_title(labels[i])
            axes[i].set_xlabel('Team 1 Goals')
            axes[i].set_ylabel('Team 2 Goals')

            # Set the x and y axis ticks to be spaced by 1 unit from 0 to 6
            axes[i].set_xticks(range(0, 7, 1))
            axes[i].set_yticks(range(0, 7, 1))

            # Set the x and y axis limits from 0 to 6
            axes[i].set_xlim(0, 6)
            axes[i].set_ylim(0, 6)

            # Add grid lines with spacing of 1 unit
            axes[i].grid(True, which='both', linestyle='-', linewidth=0.5)

            # Set minor ticks for a 1 by 1 grid
            axes[i].minorticks_on()
            axes[i].xaxis.set_minor_locator(plt.MultipleLocator(1))
            axes[i].yaxis.set_minor_locator(plt.MultipleLocator(1))

            # Add grid lines for the minor ticks
            axes[i].grid(which='minor', linestyle=':', linewidth=0.5)

        # Step 4: Adjust layout and display the plot
        plt.tight_layout()
        
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close()

        return buffer
            
    return HttpResponse(draw(pred_list), content_type='image/png')


def match_res(request):
    from collections import defaultdict
    matches = Match.objects.all()
    match_result_list = []

    for match in matches:
        match_result_list.append([match.Team_1_goals, match.Team_2_goals])
    
    match_result_list = standardize_pairs(match_result_list)

    coord_counts = defaultdict(int)
    for coord in match_result_list:
        coord_counts[tuple(coord)] += 1

    # Step 3: Prepare data for plotting
    x_vals = []
    y_vals = []
    sizes = []

    for coord in match_result_list:
        x_vals.append(coord[0])
        y_vals.append(coord[1])
        sizes.append(coord_counts[tuple(coord)] * 80)  # Adjust size multiplier as needed

    # Step 4: Plot the data
    
    plt.figure(figsize=(19, 10))

    plt.scatter(x_vals, y_vals, s=sizes, alpha=0.5, c='green')


    # plt.minorticks_on()
    plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(5))
    plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(1))

    # Add grid lines for the minor ticks
    plt.grid(which='both', linestyle=':', linewidth=0.5)
    # Customization
    plt.xlabel('Team 1 Goals')
    plt.ylabel('Team 2 Goals')
    plt.title('Scatter Plot of Scored Goals Based on Occurrences')
    plt.grid(True)


    # Step 4: Adjust layout and display the plot
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

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
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


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


