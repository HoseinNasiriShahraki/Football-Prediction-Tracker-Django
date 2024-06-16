import math
from rest_framework import serializers
from .models import Person, Match, Team, Prediction


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = "__all__"

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"

class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = "__all__"