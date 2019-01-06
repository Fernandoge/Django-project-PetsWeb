from django.db import models

# Create your models here.

class Genero(models.Model):
	GEN_COD = models.CharField(max_length=1, primary_key=True)
	GEN_NOM = models.CharField(max_length=20)