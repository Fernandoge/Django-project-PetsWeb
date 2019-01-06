from django.urls import path, include
from apps.solicitud.views import index

urlpatterns = [
     path('', index, name='solicitud'),]