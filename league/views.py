from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, "league/index.html")


def create_league(request):
    return

def my_leagues(request):
    return