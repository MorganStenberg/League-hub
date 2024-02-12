from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.db.models import F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain
from operator import attrgetter
from .models import League, Match
from .forms import CreateLeagueForm, AddMatchesForm

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
    """
    View to display all leagues that a user is a part of.
    """    
    model = League
    template_name = 'league/my_leagues.html'
    paginate_by = 6

    def get_queryset(self):
        return League.objects.all().order_by('name')


@login_required        
def user_matches(request, page=1):
    """
    View to display all matches, paginated and sorted by date, connected to a user.
    """
    
    user = request.user

    home_team_match = user.home_team_matches.all()
    away_team_match = user.away_team_matches.all()

    all_matches = sorted(
        list(chain(home_team_match, away_team_match)),
        key=attrgetter('date')
    )
    
    paginator = Paginator(all_matches, 6)
    
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)


    context = {
    'all_matches': all_matches,
    'page_obj': page_obj,
    }

    return render(request, 'league/my_matches.html', context)


@login_required
def create_league(request):

    if request.method == "POST":
        create_league_form = CreateLeagueForm(data=request.POST)
        if create_league_form.is_valid():
            create_league = create_league_form.save(commit=False)
            create_league.league_creator = request.user
            create_league.slug = slugify(create_league.name)
            create_league.save()
            messages.add_message(request, messages.SUCCESS, 'League created!')

    create_league_form = CreateLeagueForm()

    context = {
        "create_league_form": create_league_form,
    }

    return render (
        request, "league/create_league.html", context
    )


@login_required
def detailed_league(request, slug):

    """
    Displays detailed view of one league,
    including a form to add played matches to that league
    and all matches connected to that league
    """

    league_instance = get_object_or_404(League, slug=slug)
    standings = league_instance.calculate_standings()
    all_league_matches = league_instance.matches.all()
    user_matches_count = league_instance.calculate_user_matches()
    won_matches_count = league_instance.calculate_won_matches()
    lost_matches_count = league_instance.calculate_lost_matches()
    draw_matches_count = league_instance.calculate_draw_matches()


    if request.method == "POST":
        if request.user not in league_instance.league_member.all():
            messages.add_message(request, messages.ERROR, 'You can only add matches if you are a part of the league!')
            return redirect('detailed_league', slug=slug)
        add_matches_form = AddMatchesForm(data=request.POST)
        if add_matches_form.is_valid():
            add_matches = add_matches_form.save(commit=False)
            add_matches.league = league_instance
            if request.user == add_matches.home_team or request.user == add_matches.away_team:
                add_matches_form.save()
                messages.add_message(request, messages.SUCCESS, 'Match added to league!')
                standings = league_instance.calculate_standings()
                return redirect('detailed_league', slug=slug)
            else:
                messages.add_message(request, messages.ERROR, 'You can only add matches you have played!')
                return redirect('detailed_league', slug=slug)

    add_matches_form = AddMatchesForm()

    context = {
        "league_instance": league_instance,
        "standings": standings,
        "add_matches_form": add_matches_form,
        "all_league_matches": all_league_matches,
        "user_matches_count": user_matches_count,
        "won_matches_count": won_matches_count,
        "lost_matches_count": lost_matches_count,
        "draw_matches_count": draw_matches_count,
    }

    return render (
        request, "league/detailed_league.html", context
    )


@login_required
def edit_match(request, slug, match_id):
    """
    View to edit matches
    """
    league_instance = get_object_or_404(League, slug=slug)
    match = get_object_or_404(Match, pk=match_id)
  
    if request.user == match.home_team or request.user == match.away_team:
        if request.method == "POST":

            add_matches_form = AddMatchesForm(data=request.POST, instance=match)
            if add_matches_form.is_valid():
                add_matches = add_matches_form.save(commit=False)
                add_matches.league = league_instance
                add_matches_form.save()
                return redirect('detailed_league', slug=slug)
    else:
        messages.add_message(request, messages.ERROR, 'You can only edit your own matches!')

    context = {
    'slug': slug,
    "league_instance": league_instance,
    'match_id': match_id,
    'add_matches_form': AddMatchesForm(instance=match)
    }

    return render (
        request, "league/edit_match.html", context
    )


@login_required
def delete_match(request, slug, match_id):
    """
    View to delete a match
    """
    league_instance = get_object_or_404(League, slug=slug)
    match = get_object_or_404(Match, pk=match_id)
            
    if request.user == match.home_team or request.user == match.away_team:
        match.delete()

        messages.add_message(request, messages.SUCCESS, 'Match deleted!')

    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own matches!')
 
    return HttpResponseRedirect(reverse('detailed_league', args=[slug]))