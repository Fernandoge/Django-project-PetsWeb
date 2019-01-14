from django.db import models
from apps.tablas_basicas.models import Vacuna, Tipo, Genero, Desparasitacion

class Mascota(models.Model):
    foto = models.ImageField(upload_to = 'media')
    nombre = models.CharField(max_length = 50)
    edad = models.IntegerField()
    tipo = models.ForeignKey(Tipo, on_delete = models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete = models.CASCADE)
    vacuna = models.ManyToManyField(Vacuna, blank = True)
    desparasitacion = models.ForeignKey(Desparasitacion, on_delete = models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)