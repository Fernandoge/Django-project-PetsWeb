from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    edad = models.IntegerField(null=True)
    fono = models.IntegerField(null=True)
    direccion = models.CharField(max_length = 50)
    run = models.IntegerField(unique= True)
    username = models.CharField(max_length = 150, blank=True,null=True)
    USERNAME_FIELD = 'run'
    REQUIRED_FIELDS = ['username','email','first_name']

    def __str__(self):
        return '{}'.format(self.first_name)