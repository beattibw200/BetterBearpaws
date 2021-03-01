from django.urls import path, reverse
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teams/', views.TeamListView.as_view(), name='teams'),
    path('tournaments/', views.TournamentListView.as_view(), name='tournaments'),
    path('tournaments/<int:pk>', views.TournamentDetailView.as_view(), name='tournament_detail'),
    path('teams/<int:pk>', views.TeamDetailView.as_view(), name='team_detail'),
    path('signup/', views.CreateUser, name='create_user'),
    path('teams/<int:pk>', views.TeamDetailView.as_view(), name='team_detail'),
    path('createteam/', views.CreateTeamView, name='create_team'),
    path('addteamtotournament/', views.CreateParticipatesInView, name='addparticipatesin')

]
