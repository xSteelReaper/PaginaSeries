from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Anime, Manga
from .forms import AnimeForm, MangaForm

#Crud anime
class AnimeList (ListView):                    
    model = Anime
    template_name = 'Registro/anime_list.html'

class AnimeCreate (CreateView):
    model = Anime
    form_class = AnimeForm
    template_name = 'Registro/anime_form.html'
    success_url = reverse_lazy('anime_list')

class AnimeUpdate(UpdateView):
    model = Anime
    form_class = AnimeForm
    template_name = 'Registro/anime_form.html'
    success_url = reverse_lazy('anime_list')

class AnimeDelete(DeleteView):
    model = Anime
    template_name = 'Registro/anime_borrar.html'
    success_url = reverse_lazy('anime_list')

#Crud manga
class MangaList (ListView):                    
    model = Manga
    template_name = 'Registro/manga_list.html'

class MangaCreate (CreateView):
    model = Manga
    form_class = MangaForm
    template_name = 'Registro/manga_form.html'
    success_url = reverse_lazy('manga_list')

class MangaUpdate(UpdateView):
    model = Manga
    form_class = MangaForm
    template_name = 'Registro/manga_form.html'
    success_url = reverse_lazy('manga_list')

class MangaDelete(DeleteView):
    model = Manga
    template_name = 'Registro/manga_borrar.html'
    success_url = reverse_lazy('manga_list')