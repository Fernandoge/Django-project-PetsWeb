from django.views.generic.list import ListView
from apps.mascota.models import Mascota
from apps.solicitud.models import Solicitud
from django.shortcuts import render
from django.template import RequestContext, loader
from django.db.models import Q




class Inicio(ListView):	
	model = Mascota
	template_name = 'pets web/inicio.html'
	paginate_by = 3	


			