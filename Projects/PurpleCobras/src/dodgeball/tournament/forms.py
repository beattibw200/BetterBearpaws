from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.Form):
    username = forms.CharField(label='Username', max_length=60)
    password = forms.CharField(widget=forms.PasswordInput)
    choices =(
        ('Fan','Just a fan'),
        ('Participant','Participant (Coach or player)'),
        ('Manager','Tournament Manager'),
    )
    role = forms.ChoiceField(choices=choices)

    class Meta:
        model = User
        fields = ["username", "password", "role"]

from .models import Team, Tournament
class AddTeamForm(forms.Form):
    team_name = forms.CharField(label= "Team Name", max_length =100)
    team_coach = forms.CharField(label = "Coach", max_length =100)
    team_mascot = forms.CharField(label= "Mascot", max_length =100)

    class Meta:
        model = Team
        fields = ["name", "coach", "mascot"]

from .models import ParticipatesIn
class AddParticipatesIn(forms.Form):

    
    #Create form choices using above lists
    team = forms.ModelChoiceField(queryset=Team.objects.all(), required=False, help_text="Team")
    tournament = forms.ModelChoiceField(queryset=Tournament.objects.filter())
    

    class Meta:
        model = ParticipatesIn
        fields = ["team", "tournament"]
        
