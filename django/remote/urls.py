from django.urls import path
from . import views


urlpatterns = [
	path('find-game', views.find_game, name="find game"),
	path('cancel-find-game', views.cancel_find_game, name="cancel find game"),
	path('find-tournament', views.find_tournament, name="find tournament"),
]
