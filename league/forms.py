from .models import League, Match
from django import forms


class CreateLeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = ["name", "description", "league_creator", "league_member" ]
