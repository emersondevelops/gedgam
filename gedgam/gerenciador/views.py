from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Game


class GameListView(ListView):
    model = Game
    template_name = 'gerenciador/game_list.html'
    context_object_name = 'games'


class GameCreateView(CreateView):
    model = Game
    template_name = 'gerenciador/game_create.html'
    fields = '__all__'
    success_url = reverse_lazy('game_list')


class GameDeleteView(DeleteView):
    model = Game
    template_name = 'gerenciador/game_delete.html'
    success_url = reverse_lazy('game_list')


class GameUpdateView(UpdateView):
    model = Game
    template_name = 'gerenciador/game_update.html'
    fields = '__all__'
    success_url = reverse_lazy('game_list')
