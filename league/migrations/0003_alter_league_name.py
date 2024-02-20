# Generated by Django 4.2.9 on 2024-02-20 17:12

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0002_rename_league_member_league_league_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='league',
            name='name',
            field=models.CharField(max_length=200, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')]),
        ),
    ]
