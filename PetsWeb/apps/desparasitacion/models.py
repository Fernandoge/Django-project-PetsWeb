from django.db import models

# Create your models here.

class Desparasitacion(models.Model):
	DES_COD = models.CharField(max_length=2, primary_key=True)
	DES_NOM = models.CharField(max_length=45)