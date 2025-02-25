# boxeo/models.py

from django.db import models

class Boxeador(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    id_boxrec = models.CharField(max_length=20)
    imagen_url = models.URLField(null=True, blank=True)
    categoria = models.CharField(max_length=50)
    elo_actual = models.FloatField(default=1000)
    victorias = models.IntegerField(default=0)
    derrotas = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre