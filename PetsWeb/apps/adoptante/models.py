from django.db import models

from apps.usuario.models import Usuario
# Create your models here.

class Adoptante(models.Model):
	ADO_RUN = models.IntegerField(primary_key=True) 
	ADO_USU = models.ForeignKey(Usuario, null=True, blank=True, on_delete= models.CASCADE)
	ADO_NOM = models.CharField(max_length=15)	
	ADO_APELL = models.CharField(max_length=15) 	
	ADO_EDAD =	models.IntegerField() 
	ADO_FONO =	models.IntegerField() 
	ADO_MAIL =	models.EmailField(max_length=30)
	ADO_DIR =	models.CharField(max_length=20) 