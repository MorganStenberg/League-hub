from .models import League, Match
from django.contrib.auth.models import User
from django import forms


class CreateLeagueForm(forms.ModelForm):
    """
    Form for users to create a league.
    Excluding the league creator, current user, from available
    choices as league member, as they are added automatically.
    """
    class Meta:
        model = League
        fields = ["name", "description", "league_members"]

    def __init__(self, current_user=None, *args, **kwargs):
        super(CreateLeagueForm, self).__init__(*args, **kwargs)
        if current_user:
            self.fields["league_members"].queryset = (
                User.objects.exclude(pk=current_user.pk)
            )
        self.fields["league_members"].help_text = (
         "Type to start searching for other users."
         " You need to select at least one other league member."
         " The league creator is automatically added as league member."
        )


class AddMatchesForm(forms.ModelForm):
    """
    Form for users to add a match.
    Filtering the fields for home and away team,
    for users that are part of the league instance
    the match is being added to.
    Validating so that home and away team can not be the same.
    """
    class Meta:
        model = Match
        fields = ["home_team", "away_team", "home_team_score",
                  "away_team_score"]

    def __init__(self, league_instance=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if league_instance:
            self.fields['home_team'].queryset = (
                User.objects.filter(league_membership=league_instance)
                )
            self.fields['away_team'].queryset = (
                User.objects.filter(league_membership=league_instance)
                )

    def clean(self):
        cleaned_data = super().clean()
        home_team = cleaned_data.get("home_team")
        away_team = cleaned_data.get("away_team")

        if home_team == away_team:
            raise forms.ValidationError('Home team and away team cannot '
                                        'be the same.')

        return cleaned_data


class EditMatchesForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ["home_team_score", "away_team_score"]
