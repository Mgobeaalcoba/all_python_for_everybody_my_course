from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Cada clase creada acá va a ser una tabla
# Cada atributo de esa clase va a ser una columna de mi base de datos
# Para enviar la clase Tarea como base de datos a nuestro sitio debemos hacer tres cosas:
## 1. Crear el paquete migrations memdiante el comando: python manage.py makemigrations
## 2. Migrar efectivamente el modelo señalado dentro del package migrations con el comando: python manage.py migrate
## 3. Registrar nuestrom modelo en el archivo admin.py


class Tarea(models.Model):
    usuario = models.ForeignKey(User, # Está relacionado como llave foranea con la clase User
                                on_delete=models.CASCADE, # Cuando elimine un usuario debe eliminar todas sus tareas
                                null=True, # Puede contener valores nulos
                                blank=True) # Puede no completarse este valor en un formulario de la web
    titulo = models.CharField(max_length=200,
                              )
    descripcion = models.TextField(null=True,
                                   blank=True)
    completo = models.BooleanField(default=False, # Por defecto las tareas estarán incompletas hasta que se diga lo contrario
                                   )
    creado = models.DateTimeField(auto_now_add=True, # La hora y la fecha se generan de forma automatica al crear el usuario
                                  )
    def __str__(self):
        return self.titulo

    class Meta: # El nombre meta es una convención para usar esta posibilidad que nos ofrece Django
        ordering = ['completo'] # El campo o atributo llamado "completo" es el que va a determinar el orden.
