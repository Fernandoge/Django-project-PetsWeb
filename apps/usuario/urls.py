from django.urls import path

from .views import RegistroUsuario

urlpatterns = [
    path('',RegistroUsuario.as_view(), name = 'registrarAdoptante'),
]
