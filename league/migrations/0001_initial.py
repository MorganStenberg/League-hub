# Generated by Django 4.2.9 on 2024-02-02 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('league_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_leagues', to=settings.AUTH_USER_MODEL)),
                ('league_member', models.ManyToManyField(related_name='league_membership', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('home_team_score', models.PositiveIntegerField()),
                ('away_team_score', models.PositiveIntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_team_matches', to=settings.AUTH_USER_MODEL)),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_team_matches', to=settings.AUTH_USER_MODEL)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='league.league')),
            ],
        ),
    ]
