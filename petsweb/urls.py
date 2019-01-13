from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', TemplateView.as_view(template_name="pets web/inicio.html")),
    #path('listado-mascotas', TemplateView.as_view(template_name="pets web/ListadoM.html"), name= "listado-mascotas"),
    path('admin/', admin.site.urls),
    path('mascotas', include("apps.mascota.urls"), name = "listado-mascotas"),
    path('registro/', include('apps.usuario.urls'), name = "registrarAdoptante"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
