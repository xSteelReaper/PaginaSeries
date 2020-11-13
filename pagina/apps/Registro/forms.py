from .models import Anime, Manga
from django import forms

class AnimeForm(forms.ModelForm):
    

    class Meta:
        model = Anime
        fields = (
            'nombre',
            'anioPublicacion',
            'tipo',
            'sinopsis',
            'fotografia'
        )
        labels = {
            'nombre':'Nombre',
            'anioPublicacion':'Año Publicacion',
            'tipo':'Tipo',
            'sinopsis':'Sinopsis',
            'fotografia':'Fotografia'
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'anioPublicacion':forms.TextInput(attrs={'class':'form-control'}),
            'tipo':forms.Select(choices="TIPO", attrs={'class':'form-control'}),
            'sinopsis':forms.TextInput(attrs={'class':'form-control'}),
            
        }

class MangaForm(forms.ModelForm):
    

    class Meta:
        model = Manga
        fields = (
            'nombre',
            'anioPublicacion',
            'estado',
            'sinopsis',
            'fotografia'
        )
        labels = {
            'nombre':'Nombre',
            'anioPublicacion':'Año Publicacion',
            'estado':'Estado',
            'sinopsis':'Sinopsis',
            'fotografia':'Fotografia'
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'anioPublicacion':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.Select(choices="ESTADO", attrs={'class':'form-control'}),
            'sinopsis':forms.TextInput(attrs={'class':'form-control'}),
            
        }
