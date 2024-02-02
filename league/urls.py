from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('all-leagues/', views.all_leagues.as_view(), name='all_leagues'),
    path('my-leagues/', views.my_leagues.as_view(), name='my_leagues'),
    path('my-matches/', views.user_matches, name='my_matches'),
    path('create-league/', views.create_league, name='create_league'),
    #path('/', views.detailed_league, name='detailed_league')
    ]