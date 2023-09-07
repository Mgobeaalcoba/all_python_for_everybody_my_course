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

# Ejecuto las funciones decoradas

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


