from django.db import models

# Create your models here.

class Tipo_Mas (models.Model):
	TIPO_COD = models.CharField(max_length=2, primary_key=True)
	TIPO_NOM = models.CharField(max_length=20)