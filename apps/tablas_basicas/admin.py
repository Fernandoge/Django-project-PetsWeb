from django.contrib import admin
from .models import Vacuna, Tipo, Genero, Desparasitacion


admin.site.register(Vacuna)
admin.site.register(Tipo)
admin.site.register(Genero)
admin.site.register(Desparasitacion)
