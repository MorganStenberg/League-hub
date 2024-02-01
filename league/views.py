from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import League, Match
from .forms import CreateLeagueForm

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


@login_required
def create_league(request):

    if request.method == "POST":
        create_league_form = CreateLeagueForm(data=request.POST)
        if create_league_form.is_valid():
            create_league = create_league_form.save(commit=False)
            create_league.league_creator = request.user
            create_league.save()

    create_league_form = CreateLeagueForm()

    context = {
        "create_league_form": create_league_form,
    }

    return render (
        request, "league/create_league.html", context
    )



def detailed_league(request):

    """
    Displays detailed view of one league,
    including a form to add played matches to that league
    """

    if request.method == "POST":
        add_matches_form = AddMatchesForm(data=request.POST)
        if add_matches_form.is_valid():
            add_matches = add_matches_form.save(commit=False)
            
            add_matches_form.save()

    add_matches_form = AddMatchesForm()

    context = {
        "add_matches_form": add_matches_form,
    }

    return render (
        request, "league/detailed_league.html", context
    )