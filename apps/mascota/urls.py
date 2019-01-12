from django.urls import path

from .views import ListadoMascotas

urlpatterns = [
    path('', ListadoMascotas.as_view(), name='listado-mascotas'),
]
