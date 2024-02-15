from .models import League, Match
from django.contrib.auth.models import User
from django import forms


class CreateLeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = ["name", "description", "league_members"]


    def __init__(self, *args, **kwargs):
        super(CreateLeagueForm, self).__init__(*args, **kwargs)
        self.fields["league_members"].help_text = "Type to start searching for other users. You need to select at least one other league member. The league creator is automatically added as league member."


class AddMatchesForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ["home_team", "away_team", "home_team_score", "away_team_score" ]

    def __init__(self, league_instance=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if league_instance:
            self.fields['home_team'].queryset = User.objects.filter(league_membership=league_instance)
            self.fields['away_team'].queryset = User.objects.filter(league_membership=league_instance)


class EditMatchesForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ["home_team_score", "away_team_score" ]