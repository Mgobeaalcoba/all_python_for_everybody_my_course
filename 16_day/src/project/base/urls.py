from django.urls import path
from .views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea

# urlpatterns no puede mostrar clases. Por lo que a mis vistas que son clases
# debo traerlas .as_view()

urlpatterns = [
    path('', ListaPendientes.as_view(), name='tareas'), # Si voy a agregar un dominio lo debo hacer con nombre/
    path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'),
    path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
    path('editar-tarea/<int:pk>', EditarTarea.as_view(), name='editar-tarea'),
    path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name='eliminar-tarea')
]
