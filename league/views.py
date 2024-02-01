from django.shortcuts import render
from django.views import generic
from .models import League, Match

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

    def get_queryset(self):
        return League.objects.all().order_by('name')


class my_leagues(generic.ListView):
    
    model = League
    template_name = 'league/my_leagues.html'
    paginate_by = 4

    def get_queryset(self):
        return League.objects.all().order_by('name')


        
def user_matches(request):
    
    user = request.user

    home_team_match = user.home_team_matches.all()
    away_team_match = user.away_team_matches.all()

    all_matches = list(home_team_match) + list(away_team_match)

    context = {
    'all_matches': all_matches,
    }

    return render(request, 'league/my_matches.html', context)