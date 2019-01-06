from django.urls import path, include
from apps.mascota.views import index

urlpatterns = [
     path('', index, name='mascota'),]