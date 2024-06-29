from django.db import models
from django.forms import BooleanField
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Team(models.Model):
    abb = models.CharField(_("Name"), max_length=3, unique=True, primary_key=True)

    class Meta:
            verbose_name = _("Team")
            verbose_name_plural = _("Teams")
    
    def __str__(self):
        return self.abb
    
    # def get_absolute_url(self):
    #         return reverse("_detail", kwargs={"pk": self.pk})
    



class Match(models.Model):
    """Model definition for MODELNAMEMatch"""


    
    Team_1 = models.ForeignKey('Team', related_name='abb+', on_delete=models.PROTECT)
    Team_2 = models.ForeignKey('Team', related_name='abb+', on_delete=models.PROTECT)

    Team_1_goals = models.IntegerField(_("Team 1 Goals"), blank=True, null=True)
    Team_2_goals = models.IntegerField(_("Team 2 Goals"), blank=True, null=True)

    status = models.BooleanField(_("Played?"))

    title = models.CharField(_("title"), max_length=50, blank=True)

    def save(self, *args, **kwargs):
        self.title = self.Team_1.abb + ' : ' + self.Team_2.abb
        super(Match, self).save(*args, **kwargs)

    
    

    def __str__(self):
        return self.title
    

    # TODO: Define fields here

    class Meta:
        
        """Meta definition for MODELNAMEMatch"""

        verbose_name = 'Match'
        verbose_name_plural = 'Matches'



class Person(models.Model):

    name = models.CharField(_("Name"), max_length=50, unique=True)

    points = models.IntegerField(_("points"), blank=True, default=0)

    history = models.CharField(_("history points"), max_length=5000,default='0,')

    
    

    class Meta:
        """Meta definition for Person."""
        ordering = ('-points',)
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

    def __str__(self):
        return self.name




class Prediction(models.Model):
    """Model definition for MODELNAME."""



    person = models.ForeignKey('Person', related_name='name+', on_delete=models.CASCADE)
    match = models.ForeignKey('Match', related_name='title+', on_delete=models.CASCADE)
    Team_1_pred = models.PositiveSmallIntegerField(_("Team 1 Prediction"))
    Team_2_pred = models.PositiveSmallIntegerField(_("Team 2 Prediction"))
    persons_name = models.CharField(_("Predictor's name"), max_length=50, default="")
    match_title = models.CharField(_("Match Title"), max_length=50, default="")



    calculated = models.BooleanField(_("Is Calculated"), default=False)

    # def save(self, *args, **kwargs):
        # self.persons_name = self.person.name
        # super(Prediction, self).save(*args, **kwargs)




    def __str__(self):
        return f'{self.person.name} - {self.match.title}'

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Prediction'
        verbose_name_plural = 'Predictions'



def calculate_points():
    from .models import Prediction, Match
    from .models import Person
    # Create your views here.

    all_preds = Prediction.objects.all()

    for pred in all_preds:
        if pred.calculated == False:
            person = Person.objects.get(name=pred.person.name)
            match = Match.objects.get(title=pred.match.title)

            if match.status == False:
                continue

            pred_t1 = pred.Team_1_pred
            pred_t2 = pred.Team_2_pred

            result_t1 = match.Team_1_goals
            result_t2 = match.Team_2_goals

            winner = ''
            pred_winner = ''

            if pred_t1 > pred_t2:
                pred_winner = 't1'
            elif pred_t2 > pred_t1:
                pred_winner = 't2'
            else:
                pred_winner = 'none'

            if result_t1 > result_t2:
                winner = 't1'
            elif result_t2 > result_t1:
                winner = 't2'
            else:
                winner = 'none'

            if pred_t1 == result_t1 and pred_t2 == result_t2 and pred_winner == winner:
                person.points += 10
                person.history += str(person.points)+','
                person.save()

            elif abs(pred_t1 - pred_t2) == abs(result_t1 - result_t2) and pred_winner == winner:
                person.points += 7
                person.history += str(person.points)+','
                person.save()
            elif winner == pred_winner:
                person.points += 5
                person.history += str(person.points)+','
                person.save()
            else:
                person.history += str(person.points)+','
                person.save()
            
            pred.calculated = True
            pred.save()

calculate_points()

def Pred_name_save():
    from .models import Prediction, Person
    preds = Prediction.objects.all()
    for pred in preds:
        pred.persons_name = pred.person.name
        pred.match_title = pred.match.title
        pred.save()

Pred_name_save() 