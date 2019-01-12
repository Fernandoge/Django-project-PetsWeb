from django.views.generic.list import ListView
from .models import Mascota

class ListadoMascotas(ListView):
	model = Mascota
	template_name = 'pets web/ListadoM.html'
	paginate_by = 20

