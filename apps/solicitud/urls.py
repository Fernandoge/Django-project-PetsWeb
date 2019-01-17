from django.urls import path

from .views import CrearSolicitud

urlpatterns = [
    path('', CrearSolicitud.crear, name='crearSolicitud'),

]
    