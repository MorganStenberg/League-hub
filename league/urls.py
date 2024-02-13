from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('all-leagues/', views.all_leagues.as_view(), name='all_leagues'),
    path('my-leagues/', views.my_leagues, name='my_leagues'),
    path('my-matches/', views.user_matches, name='my_matches'),
    path('create-league/', views.create_league, name='create_league'),
    path('<slug:slug>/', views.detailed_league, name='detailed_league'),
    path('<slug:slug>/edit_match/<int:match_id>', views.edit_match, name='edit_match'),
    path('<slug:slug>/delete_match/<int:match_id>', views.delete_match, name='delete_match'),
    ]