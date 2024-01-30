from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import League, Match

# Register your models here.

admin.site.register(League)
admin.site.register(Match)