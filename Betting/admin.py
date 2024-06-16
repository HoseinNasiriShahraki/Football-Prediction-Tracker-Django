from django.contrib import admin
from .models import Person, Match, Team, Prediction
# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    list_display = ['abb']
admin.site.register(Team, TeamAdmin)


class MatchAdmin(admin.ModelAdmin):
    list_display = ('title', 'Team_1', 'Team_1_goals', 'Team_2', 'Team_2_goals', 'status')
admin.site.register(Match, MatchAdmin)


class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'points']
admin.site.register(Person, PersonAdmin)


class PredictionAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'Team_1_pred', 'Team_2_pred', 'calculated']
    list_filter = ['person']
admin.site.register(Prediction, PredictionAdmin)