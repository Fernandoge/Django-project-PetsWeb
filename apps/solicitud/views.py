from django.http import HttpResponse
from .models import Solicitud
from apps.usuario.models import User
from apps.mascota.models import Mascota
from apps.tablas_basicas.models import Estado
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.template import RequestContext, loader

class CrearSolicitud:

    def crear(request, mascotaid):
        Solicitud.objects.create(adoptante = User.objects.get(run = request.user.get_username()), mascota = Mascota.objects.get(id = mascotaid), estado = Estado.objects.get(nombre = 'Pendiente'))
        context = RequestContext(request,{

	    })
        return render(request, 'pets web/solicitudes.html', locals())
        
