from django.db import models
from django.contrib.auth.models import User
from django.db.models import F

# Create your models here.

class League(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    league_creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_leagues"
    )
    league_member = models.ManyToManyField(
        User, related_name="league_membership"
    )


    # Calculates the league standing based on points in matches
    def calculate_standings(self):
        user_points = {}


        for match in self.matches.all():

            home_team = match.home_team
            away_team = match.away_team

            home_points, away_points = match.calculate_points()

            user_points[home_team] = user_points.get(home_team, 0) + home_points
            user_points[away_team] = user_points.get(away_team, 0) + away_points



        league_standings = sorted(user_points.items(), key=lambda x: x[1], reverse=True)

        return league_standings


    # Calculates the number of matches each user has played 
    def calculate_user_matches(self):
        user_matches_played = {}

        for match in self.matches.all():

            home_team = match.home_team
            away_team = match.away_team

            user_matches_played[home_team] = user_matches_played.get(home_team, 0) + 1
            user_matches_played[away_team] = user_matches_played.get(away_team, 0) + 1

        return user_matches_played


    # Calculates the number of matches won by each user
    def calculate_won_matches(self):

        user_matches_won = {}

        for user in self.league_member.all():
            won_matches_count = self.matches.filter(
                home_team=user, home_team_score__gt=F('away_team_score')
            ).count() + self.matches.filter(
                away_team=user, away_team_score__gt=F('home_team_score')
            ).count()
            user_matches_won[user] = won_matches_count

        return user_matches_won


    # Calculates the number of matches lost by each user
    def calculate_lost_matches(self):

        user_matches_lost = {}

        for user in self.league_member.all():
            lost_matches_count = self.matches.filter(
                home_team=user, home_team_score__lt=F('away_team_score')
            ).count() + self.matches.filter(
                away_team=user, away_team_score__lt=F('home_team_score')
            ).count()
            user_matches_lost[user] = lost_matches_count

        return user_matches_lost




    def __str__(self):
        return self.name


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


    def calculate_points(self):
        win_points = 3
        draw_points = 1
        loss_points = 0

        if self.home_team_score > self.away_team_score:
            home_points = win_points 
            away_points = loss_points 
        elif self.home_team_score < self.away_team_score: 
            home_points = loss_points
            away_points = win_points
        else:
            home_points = draw_points
            away_points = draw_points

        return home_points, away_points

