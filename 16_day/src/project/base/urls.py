from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pendientes, name='pendientes'), # Si voy a agregar un dominio lo debo hacer con nombre/

]
