from django.db import models

"""Vacunas que han recibido las mascotas"""
class Vacuna(models.Model):
    nombre = models.CharField(max_length = 50)

    def __str__(self):
        return '{}'.format(self.nombre)

"""Tipo de mascota"""
class Tipo(models.Model):
    nombre = models.CharField(max_length = 50)

    def __str__(self):
        return '{}'.format(self.nombre)

"""Generos de las mascotas"""
class Genero(models.Model):
    nombre = models.CharField(max_length = 50)

    def __str__(self):
        return '{}'.format(self.nombre)

"""Desparasitación que han recibido las mascotas"""
class Desparasitacion(models.Model):
    nombre = models.CharField(max_length = 50)

    def __str__(self):
        return '{}'.format(self.nombre)
