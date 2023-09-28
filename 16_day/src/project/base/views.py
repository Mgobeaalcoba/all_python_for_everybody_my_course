from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# FormView, UserCreationForm y la función login son las necesarias para crear un nuevo usuario desde nuestra Web App
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
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

class PaginaRegistro(FormView):
    template_name = 'base/registro.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tareas')

    # Sobreescribimos un método para que el usuario ya quede logueado luego del registro:
    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(PaginaRegistro, self).form_valid(form)

    # Sobreescribo el método "get" para que funcione el redireccionamiento en el caso de querer ir a "registrarse" estando logueado
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tareas')
        return super(PaginaRegistro, self).get(*args, **kwargs)

class ListaPendientes(LoginRequiredMixin, ListView):
    model = Tarea
    context_object_name = 'tareas' # Con este nombre llamo a mi ListaPendientes en mi template HTML

    # Sobreescribimos get_context_data para que solo nos traiga las tareas del user logueado:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tareas"] = context["tareas"].filter(usuario=self.request.user)
        context["count"] = context["tareas"].filter(completo=False).count()

        # Agregamos lógica para que solo muestre las tareas que el usuario mostró en la caja de texto:
        valor_buscado = self.request.GET.get('area-buscar')
        if valor_buscado:
            context['tareas'] = context['tareas'].filter(titulo__icontains=valor_buscado)

        context['valor_buscado'] = valor_buscado

        return context

class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    context_object_name = 'tarea'
    template_name = 'base/tarea.html' # Cambio el nombre por default que va a buscar Django para renderizar

# Con la clase CreateView le damos la posibilidad al usuario de crear nuevos elementos en las listas:
class CrearTarea(LoginRequiredMixin, CreateView):
    # Create View tomará la clase que pasemos como Modelo y creará un formulario basado en los campos que tiene nuestra clase modelo
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo'] # Le estamos indicando que queremos renderizar todos los campos.
    success_url = reverse_lazy('tareas') # le paso el nombre de nuestra url que es la principal para que redirija

    # Sobreescribo el método form_valid para que directamente asigne la tarea al user logueado sin preguntar:
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(CrearTarea, self).form_valid(form)

class EditarTarea(LoginRequiredMixin, UpdateView):
    # No necesita un template nuevo dado que utiliza el mismo que ya tenemos para CrearTarea.
    # También carga la info que la tarea tiene en cada uno de sus campos/atributos
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo']
    success_url = reverse_lazy('tareas')

class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    context_object_name = 'tarea'
    success_url = reverse_lazy('tareas')
