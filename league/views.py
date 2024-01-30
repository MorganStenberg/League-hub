from django.shortcuts import render
from django.views import generic
from .models import League

# Create your views here.

def home_page(request):
    return render(request, "league/index.html")

class all_leagues(generic.ListView):
    """
    Displays a list of all leagues created. 

    todo: add queryset to filter for active leagues 
        if feature of season based leagues is added 
    """
    model = League
    template_name = 'league/all_leagues.html'
    paginate_by = 4

