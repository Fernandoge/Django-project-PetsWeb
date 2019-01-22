from django.urls import path

from .views import ListadoMascota

urlpatterns = [
    #path('', ListadoMascotas.as_view(), name='listado-mascotas'),
    #path('', Inicio.as_view(), name='inicio'),
    path('', ListadoMascota, name='listado-mascotas'),

    
    
]
