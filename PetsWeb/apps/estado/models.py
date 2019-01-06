from django.db import models

# Create your models here.

class Estado(models.Model):
	EST_COD = models.CharField(max_length=3, primary_key=True)
	EST_NOM = models.CharField(max_length=20)