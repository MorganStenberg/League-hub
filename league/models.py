from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class League(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    league_creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_leagues"
    )
    league_member = models.ManyToManyField(
        User, related_name="league_membership"
    )



class Match(models.Model):
    """

    """
    league = models.ForeignKey(
        League, on_delete=models.CASCADE, related_name="matches"
    )
    date = models.DateTimeField(auto_now_add=True)
    home_team = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="home_team_matches"
    )
    away_team = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="away_team_matches"
    )
    home_team_score = models.PositiveIntegerField()
    away_team_score = models.PositiveIntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    #def calculate_points(self):
        #win_points = 3
        #draw_points = 1
       # loss_points = 0
