from django.db import models

TIPO = (
    ('Shounen', 'Shounen'),
    ('Shoujo', 'Shoujo'),
    ('Seinen', 'Seinen'),
    ('Josei', 'Josei'),
)

class Anime(models.Model):
    nombre = models.CharField(max_length=100)
    anioPublicacion = models.IntegerField()
    tipo = models.CharField(max_length=50, choices=TIPO)
    sinopsis = models.CharField(max_length=200)
    fotografia = models.ImageField(upload_to='catalogo_anime', blank=True)
    
    def __str__(self):
        return str(self.fotografia)

ESTADO = (
    ('Emision', 'Emision'),
    ('Finalizado', 'Finalizado'),
)

class Manga(models.Model):
    nombre = models.CharField(max_length=100)
    anioPublicacion = models.IntegerField()
    estado = models.CharField(max_length=50, choices=ESTADO)
    sinopsis = models.CharField(max_length=200)
    fotografia = models.ImageField(upload_to='catalogo_manga', blank=True)
    
    def __str__(self):
        return str(self.fotografia)
