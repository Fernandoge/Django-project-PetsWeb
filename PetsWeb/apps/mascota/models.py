from django.db import models

from apps.genero.models import Genero
from apps.tipo_mas.models import Tipo_Mas
from apps.desparasitacion.models import Desparasitacion

class Vacuna(models.Model):
	VAC_ID = models.IntegerField(primary_key=True)
	VAC_NOM = models.CharField(max_length=50)

class Mascota(models.Model):
	MAS_ID = models.IntegerField(primary_key=True)
	MAS_NOM = models.CharField(max_length=15)
	MAS_TIPO = models.ForeignKey(Tipo_Mas, null=True, blank=True, on_delete= models.CASCADE)
	MAS_GEN = models.ForeignKey(Genero, null=True, blank=True, on_delete= models.CASCADE)
	MAS_DES = models.ForeignKey(Desparasitacion, null=True, blank=True, on_delete= models.CASCADE)
	MAS_EDAD = models.IntegerField()
	MAS_VAC = models.ManyToManyField(Vacuna)


