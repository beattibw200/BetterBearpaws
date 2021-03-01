from django.contrib import admin
from .models import Tournament, Team, Match, ParticipatesIn

admin.site.register(Tournament)
admin.site.register(Match)
admin.site.register(Team)
admin.site.register(ParticipatesIn)
