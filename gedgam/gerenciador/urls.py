from django.urls import path
from .views import GameListView, GameCreateView

urlpatterns = [
    path('', GameListView.as_view(), name='game_list'),
    path('adicionar/', GameCreateView.as_view(), name='game_create'),
]
