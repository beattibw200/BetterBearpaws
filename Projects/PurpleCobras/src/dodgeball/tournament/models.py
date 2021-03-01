from django.db import models
from django.db.models import Q
from django.urls import reverse

class Tournament(models.Model):
    title = models.CharField(max_length=100)
    date_of = models.DateField(help_text='Date')
    completed = models.BooleanField(default=False)
    teams = models.ManyToManyField(to='Team', through='ParticipatesIn')

    class Meta:
        ordering = ['date_of']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tournament_detail', args=[str(self.id)])

class ParticipatesIn(models.Model):
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
        

class Team(models.Model):
    name = models.CharField(max_length=100)
    coach = models.CharField(max_length=100)
    mascot = models.CharField(max_length=100)

    @property
    def matches(self):
        return Match.objects.filter(Q(team_1=self) | Q(team_2=self))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('team_detail', args=[str(self.id)])


class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    round_index = models.IntegerField()

    team_1 = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="team_1_matches", related_query_name="team_1_match")
    team_2 = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="team_2_matches", related_query_name="team_2_match")

    score_1 = models.IntegerField(help_text='Team 1 eliminations', null=True, blank=True)
    score_2 = models.IntegerField(help_text='Team 2 eliminations', null=True, blank=True)

    @property
    def winning_team(self):
        if (self.score_1==5 or self.score_2==5):
            if self.score_1 == 5 and self.score_2 < 5:
                return self.team_1
            if self.score_2 == 5 and self.score_1 < 5:
                return self.team_2
        return None

    @property
    def match_over(self):
        if score_1 and score_2:
            if score_1 == 5 or score_2 == 5:
                return True
        return False

    def __str__(self):
        return f'{self.tournament.title} (round {self.round_index}): {self.team_1.name} vs {self.team_2.name}'


    
