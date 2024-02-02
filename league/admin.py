from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import League, Match

# Register your models here.

@admin.register(League)
class LeagueAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug', 'league_creator')
    search_fields = ['name', 'league_creator']
    prepopulated_fields  = {'slug': ('name',)}
    summernote_field = ('description')

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('league', 'date', 'home_team', 'away_team', 'home_team_score', 'away_team_score')
    search_fields = ['home_team', 'away_team']