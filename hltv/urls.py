from django.conf.urls import url
from .views import get_players

urlpatterns = [
    url(r'players/', get_players, name='get_players'),
]
