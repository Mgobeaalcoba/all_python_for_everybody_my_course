from django.urls import path
from .views import ListaPendientes, DetalleTarea

# urlpatterns no puede mostrar clases. Por lo que a mis vistas que son clases
# debo traerlas .as_view()

urlpatterns = [
    path('', ListaPendientes.as_view(), name='pendientes'), # Si voy a agregar un dominio lo debo hacer con nombre/
    path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea')
]
