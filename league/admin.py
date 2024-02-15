from django.contrib import admin
from .models import League, Match

# Register your models here.

@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'league_creator')
    search_fields = ['name', 'league_creator__username']
    prepopulated_fields  = {'slug': ('name',)}
    autocomplete_fields = ['league_members']

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('league', 'date', 'home_team', 'away_team', 'home_team_score', 'away_team_score')
    search_fields = ['home_team__username', 'away_team__username']