from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('all-leagues/', views.all_leagues.as_view(), name='all_leagues')
    ]