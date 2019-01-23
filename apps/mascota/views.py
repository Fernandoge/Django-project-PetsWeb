from django.views.generic.list import ListView
from .models import Mascota
from apps.solicitud.models import Solicitud
from django.shortcuts import render
from django.template import RequestContext, loader
from django.db.models import Q


#class ListaMascotas(ListView):	
#	model = Mascota
#	template_name = 'pets web/inicio.html'
#	paginate_by = 3	


#Se creo una nueva función para usar dos modelos

def ListadoMascota(request):
	
	mascotas_sin_solicitud = Mascota.objects.all()
	criterion1 = Q(estado__nombre = 'Pendiente')
	criterion2 = Q(estado__nombre = 'Aceptada')
	mascotas_pendientes_aceptadas = Solicitud.objects.filter(criterion1 | criterion2).values_list('mascota', flat = True)
	mascotas_rechazadas = Solicitud.objects.filter(estado__nombre = 'Rechazada').order_by('mascota').distinct('mascota').exclude(mascota__in=mascotas_pendientes_aceptadas)
	#mascotas_rechazadas = solicitudes_rechazadas.orderby(mascota).distinct(mascota)

	context = RequestContext(request,{
		'mascotas_sin_solicitud': mascotas_sin_solicitud,
		'mascotas_rechazadas': mascotas_rechazadas,
	})
	return render(request, 'pets web/ListadoM.html', locals())


			