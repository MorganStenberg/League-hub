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



admin.site.register(Match)