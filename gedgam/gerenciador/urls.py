from django.urls import path
from .views import GameListView, GameCreateView, GameDeleteView, GameUpdateView

urlpatterns = [
    path('', GameListView.as_view(), name='game_list'),
    path('adicionar/', GameCreateView.as_view(), name='game_create'),
    path('remover/<int:pk>', GameDeleteView.as_view(), name='game_delete'),
    path('editar/<int:pk>', GameUpdateView.as_view(), name='game_update')
]
