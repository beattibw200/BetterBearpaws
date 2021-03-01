from django.shortcuts import render
from django.views import generic

# Create your views here.

def index(request):
    tournaments_list = Tournament.objects.order_by('date_of')
    context = {
        'tournaments_list': tournaments_list,
    }
    return render(request, 'index.html', context=context)

from .forms import SignupForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import login

def CreateUser(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            role = form.cleaned_data.get('role')
            user = User.objects.create_user(username=username, password=password)
            group = (Group.objects.get(name=role),)
            user.groups.set(group)
            user.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

from django.views import generic
from django.shortcuts import render
from tournament.models import *
from .forms import AddTeamForm
from django.http import HttpResponseRedirect

class TeamListView(generic.ListView):
    model = Team

class TournamentListView(generic.ListView):
    model = Tournament

class TeamDetailView(generic.DetailView):
    model = Team

class TournamentDetailView(generic.DetailView):
    model = Tournament

def CreateTeamView(request):
    if request.method == 'POST':
        form = AddTeamForm(request.POST)
        if form.is_valid():
            team_name = form.cleaned_data.get('team_name')
            team_coach = form.cleaned_data.get('team_coach')
            team_mascot = form.cleaned_data.get('team_mascot')
            newteam = Team.objects.create(name= team_name, coach= team_coach, mascot= team_mascot)
            newteam.save()
            return HttpResponseRedirect('/tournament/teams')

    else:
        form = AddTeamForm()

    return render(request, "tournament/add_team.html", {'form': form})

from .forms import AddParticipatesIn
def CreateParticipatesInView(request):
    if request.method == 'POST':
        form = AddParticipatesIn(request.POST)
        if form.is_valid():
            teamname = form.cleaned_data.get('team')
            team = Team.objects.get(name=teamname)
            tournamentname = form.cleaned_data.get('tournament')
            tournament = Tournament.objects.get(title=tournamentname)

            newParticipatesIn = ParticipatesIn.objects.create(team= team, tournament= tournament)
            newParticipatesIn.save()
            return HttpResponseRedirect('/')
    else:
        form = AddParticipatesIn()

    return render(request, "tournament/add_participatesin.html", {'form': form})
