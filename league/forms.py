from .models import League, Match
from django import forms


class CreateLeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = ["name", "description", "league_member" ]


class AddMatchesForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ["home_team", "away_team", "home_team_score", "away_team_score" ]
