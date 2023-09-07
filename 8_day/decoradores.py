"""
Los decoradores son patrones de diseño en Python utilizados
para dar nueva funcionalidad a objetos (funciones),
modificando su comportamiento sin alterar su estructura: son
funciones que modifican funciones.

Las funciones en Python soportan operaciones tales como ser asignadas a una
variable, pasadas como argumento, y ser devueltas por otra función como resultado.
También, es posible definir funciones dentro de funciones, sin que estén disponibles
fuera de la función dentro de la cual fueron definidas.
Los decoradores permiten que una función se modifique ante determinados
escenarios, sin duplicar código.
"""

def mostrar_informacion(funcion):
    def interior():
        print(f'Ejecutando la función {funcion.__name__}')
        funcion()
        print('Ejecución finalizada')
    return interior

# 1° Forma de usar el decorador: 

@mostrar_informacion
def impresion():
    print("Hola Mundo")


impresion()

"""
Ejecutando la funci�n impresion
Hola Mundo
Ejecuci�n finalizada
"""

# 2° Forma de usar el decorador:

def impresion2():
    print("Hola Mundo")


funcion_decorada = mostrar_informacion(impresion2)
funcion_decorada()

"""
Ejecutando la función impresion
Hola Mundo
Ejecución finalizada
"""