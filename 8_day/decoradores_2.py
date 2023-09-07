def decorar_saludo(funcion): # Recive una funcion que es la que va a decorar
    def otra_funcion_interna(palabra): # Recibe la palabra que queremos decorar
        print("hola")
        funcion(palabra) # Llamo a la función que estoy decorando para que realice su tarea. Por ejemplo: imprimir una palabra
        print("adios")
    return otra_funcion_interna # Ejecuta la función interna como unica acción propia de la función padre


# Funciones que voy a decorar luego: 

def mayuscula(texto):
    print(texto.upper())


def minuscula(texto):
    print(texto.lower())


# Ejecuto las funciones sin decorar:
mayuscula("python")
minuscula("PYTHON")

"""
PYTHON
python
"""

# Ejecuto las funciones decoradas sin poner el decorador propiamente dicho arriba de la funcion "@decorar_saludo"

mayuscula_decorada = decorar_saludo(mayuscula)
mayuscula_decorada("python")

minuscula_decorada = decorar_saludo(minuscula)
minuscula_decorada("PYTHON")

"""
hola
PYTHON
adios
hola
python
adios
"""

# Para poder usar los decoradores en caracter obligatorio entonces haría: 

def decorar_saludo2(funcion): # Recive una funcion que es la que va a decorar
    def otra_funcion_interna(palabra): # Recibe la palabra que queremos decorar
        print("hola")
        funcion(palabra) # Llamo a la función que estoy decorando para que realice su tarea. Por ejemplo: imprimir una palabra
        print("adios")
    return otra_funcion_interna # Ejecuta la función interna como unica acción propia de la función padre


# Funciones que voy a decorar luego: 
@decorar_saludo2
def mayuscula2(texto):
    print(texto.upper())

@decorar_saludo2
def minuscula2(texto):
    print(texto.lower())


# Ejecuto las funciones sin decorar:
mayuscula2("python")
minuscula2("PYTHON")

"""
hola
PYTHON
adios
hola
python
adios
"""