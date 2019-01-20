from django.db import models
from apps.tablas_basicas.models import Estado
from apps.usuario.models import User
from apps.mascota.models import Mascota

# Create your models here.

class Solicitud(models.Model):
    adoptante = models.ForeignKey(User, on_delete = models.CASCADE)
    mascota = models.ForeignKey(Mascota, on_delete = models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete = models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {} {}'.format(self.mascota,self.adoptante,self.estado)