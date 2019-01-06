from django.db import models

from apps.adoptante.models import Adoptante
from apps.mascota.models import Mascota
from apps.estado.models import Estado


class Solicitud(models.Model):
	SOL_ID = models.IntegerField(primary_key=True)
	SOL_RUN = models.ForeignKey(Adoptante, null=True, blank=True, on_delete= models.CASCADE)
	SOL_MAS = models.OneToOneField(Mascota, null=True, blank=True, on_delete=models.CASCADE)
	SOL_EST = models.ForeignKey(Estado, null=True, blank=True, on_delete=models.CASCADE)
	SOL_FEC = models.DateField()