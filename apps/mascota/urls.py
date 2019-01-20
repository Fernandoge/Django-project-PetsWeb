from django.urls import path

#from .views import ListadoMascotas
from .views import ListadoMascota

urlpatterns = [
    #path('', ListadoMascotas.as_view(), name='listado-mascotas'),
    path('', ListadoMascota, name='listado-mascotas'),
    
]
