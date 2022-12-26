from django.db import models

class LibrosRestApi(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()