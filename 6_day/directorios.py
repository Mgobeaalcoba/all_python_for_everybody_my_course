# Usar Path y OS es clave para compatibilizar nuesto producto con cualquier sistema operativo
import os

ruta = os.getcwd() # Obtiene el directorio de trabajo actual
print(ruta) # c:\Users\mgobea\Documents\develop\python_total\6_day

# Si necesito abrir archivos que se encuentran en una ruta distinta de trabajo entonces debo usar "change directory" o os.chdir()

# Busco, copio y pego el directorio con el que quiero trabajar y le agrego dobles barras invertidas al mismo si es Windows
ruta2 = os.chdir("C:\\Users\\mgobea\\Desktop\\Alternativo")
print(ruta2) # None no tengo nada en ruta2 dado que cambio el directorio pero no estoy guardando nada en la variable
ruta2 = os.getcwd()
print(ruta2) # C:\Users\mgobea\Desktop\Alternativo --> Compruebo que efectivamente Python ya se ubica actualmente en otro directorio
my_file = open("Otro_archivo.txt", "r")
print(my_file.read())
"""
Un archivo
Alternativo
para trabajar 
con OS y Path
"""

# Crear directorios:

import os

os.makedirs("C:\\Users\\mgobea\\Desktop\\Alternativo\\NuevoDictPython2") # Se creo efectivamente la carpeta dentro del directorio en el que estaba ubicado, pero podría haberlo creado donde quisiera. 

# Visualizo el contenido de mi actual directorio para comprobar por código también la creación de la carpeta: 

os.chdir("C:\\Users\\mgobea\\Desktop\\Alternativo")

contenido_directorio = os.listdir()

print(contenido_directorio)

for item in contenido_directorio:
    print(item)

"""
['NuevoDictPython', 'NuevoDictPython2', 'Otro_archivo.txt']
NuevoDictPython
NuevoDictPython2
Otro_archivo.txt
"""

# Encontrar el nombre de base de nuestra ruta o el nombre completo del directorio donde se aloja un archivo: 

import os

ruta = "C:\\Users\\mgobea\\Desktop\\Alternativo\\Otro_archivo.txt"

basename = os.path.basename(ruta)
print(basename) # Otro_archivo.txt

dirname = os.path.dirname(ruta)
print(dirname) # C:\Users\mgobea\Desktop\Alternativo

# También podría requerir basename y dirname en una tupla así:

split = os.path.split(ruta)
print(split) # ('C:\\Users\\mgobea\\Desktop\\Alternativo', 'Otro_archivo.txt')

# También podemos eliminar carpetas: rmdir

import os

os.rmdir("C:\\Users\\mgobea\\Desktop\\Alternativo\\NuevoDictPython2")

os.chdir("C:\\Users\\mgobea\\Desktop\\Alternativo")

contenido_directorio = os.listdir()

for item in contenido_directorio:
    print(item)


# Uso de Path de pathlib para compatibilizar los sistemas operativos: 

from pathlib import Path

carpeta = Path("C:/Users/mgobea/Desktop/Alternativo") # Para trabajar con paths agnosticos cambio las barras invertidas de windows por barras normales. 
archivo = carpeta / "Otro_archivo.txt" # Forma de concatenar rutas usando objetos Path.

# Al crear la ruta desde Path permito que cualquier sistema que abra este archivo lo pueda entender, ya sea que usa Windows, o Mac o Linux. 

my_file = open(archivo,"r")
print(my_file.read())

"""
Un archivo
Alternativo
para trabajar 
con OS y Path
"""

# Esta es la forma correcta de trabajar con directorios de forma profesional. 
