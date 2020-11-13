from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login_required
from .views import AnimeList, AnimeCreate, AnimeUpdate , AnimeDelete
from .views import MangaList, MangaCreate, MangaUpdate , MangaDelete

urlpatterns = [
    path('listar_anime/', AnimeList.as_view(), name="anime_list"),
    path('crear_anime/', AnimeCreate.as_view(), name="anime_form"),
    path('editar_anime/<int:pk>', login_required(AnimeUpdate.as_view()), name="anime_update"),
    path('borrar_anime/<int:pk>', login_required(AnimeDelete.as_view()), name="anime_borrar"),
    
    
    path('listar_manga/', MangaList.as_view(), name="manga_list"),
    path('crear_manga/', MangaCreate.as_view(), name="manga_form"),
    path('editar_manga/<int:pk>', login_required(MangaUpdate.as_view()), name="manga_update"),
    path('borrar_manga/<int:pk>', login_required(MangaDelete.as_view()), name="manga_borrar"),
    
]
