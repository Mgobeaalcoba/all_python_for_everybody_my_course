from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
# LoginRequiredMixin no se hereda en una nueva clase sino en clases ya existentes:
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Tarea

# Tipo de pagina que representa una lista de objetos
# Se puede usar para mostrar una lista completa traida de una database o una lista filtrada
# Tengo que tener previamente una plantilla html para poder renderizar la view
# El directorio de mis plantillas HTML debe estar declarado en mi archivo project/settings.py en la sección TEMPLATES
# Y tengo que tener tareas en mi base de datos que las voy a cargar vía Django Admin

# Las vistas pueden ser funciones o clases. Si usamos templates de Django deben ser clases:

class Logueo(LoginView):
    template_name = "base/login.html"
    field = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        """ Cuando el usuario esté logueado
        se lo redirigirá directamente a la pagina
        de tareas """
        return reverse_lazy('tareas')

class ListaPendientes(LoginRequiredMixin, ListView):
    model = Tarea
    context_object_name = 'tareas' # Con este nombre llamo a mi ListaPendientes en mi template HTML

class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    context_object_name = 'tarea'
    template_name = 'base/tarea.html' # Cambio el nombre por default que va a buscar Django para renderizar

# Con la clase CreateView le damos la posibilidad al usuario de crear nuevos elementos en las listas:
class CrearTarea(LoginRequiredMixin, CreateView):
    # Create View tomará la clase que pasemos como Modelo y creará un formulario basado en los campos que tiene nuestra clase modelo
    model = Tarea
    fields = '__all__' # Le estamos indicando que queremos renderizar todos los campos.
    success_url = reverse_lazy('tareas') # le paso el nombre de nuestra url que es la principal para que redirija

class EditarTarea(LoginRequiredMixin, UpdateView):
    # No necesita un template nuevo dado que utiliza el mismo que ya tenemos para CrearTarea.
    # También carga la info que la tarea tiene en cada uno de sus campos/atributos
    model = Tarea
    fields = '__all__'
    success_url = reverse_lazy('tareas')

class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    context_object_name = 'tarea'
    success_url = reverse_lazy('tareas')
