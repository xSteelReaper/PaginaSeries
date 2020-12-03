from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Anime, Manga
from .forms import AnimeForm, MangaForm

# las importaciones para la API 
from rest_framework import generics
from .serializers import AnimeSerializer
from .serializers import MangaSerializer


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
    
    
# clases para la Api 
# Anime
class API_objects_Anime(generics.ListCreateAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    
class API_objects_details_Anime(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer

# # Manga
class API_objects_Manga(generics.ListCreateAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    
class API_objects_details_Manga(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
