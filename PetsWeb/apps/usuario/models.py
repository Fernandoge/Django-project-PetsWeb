from django.db import models

# Create your models here.

class Usuario(models.Model):
	USU_COD = models.IntegerField(primary_key=True)
	USU_NOM = models.CharField(max_length=20)