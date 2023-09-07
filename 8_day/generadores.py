"""
Los generadores son tipos especiales de funciones que
devuelven un iterador que no almacena su contenido
completo en memoria, sino que "demora" la ejecución de una
expresión hasta que su valor se solicita.

Dado que un ordenador no cuenta con memoria
infinita, no podría generarse una secuencia de
números sin límite sin la ayuda de un generador

Lo mismo ocurre con datos que, sin ser infinitos,
ocuparían demasiado espacio en memoria de
almacenarse repentinamente

¿Que hace una función generadora?
- Cuida el espacio en memoría de mi ordenador
- Optimiza la memoria requerida para ejecutar codigo. 
"""

# Ejemplo de un generador
def secuencia_infinita():
    num = 0
    while True:
        yield num # yield quiere decir producir. Es muy distinto a return // el generador recuerda cual fue el último valor producido
        num += 1

generador = secuencia_infinita()

for i in range(100):
    print(next(generador)) # Imprimirá hasta el 99 de a 1 numero por linea

print(next(generador)) # Imprimirá el 100
print(next(generador)) # Imprimirá el 101

def mi_funcion():
    return 4


def mi_generador():
    yield 4


print(mi_funcion()) # 4
print(mi_generador()) # <generator object mi_generador at 0x000001DD6C639430>

# El generador no devuelve el 4 porque aún no le hemos pedido que lo produzca. 

print(next(mi_generador())) # 4 encerrando mi generador entre un next() le solicito que genera el valor que va en yield

# Ejemplo de aplicación: Retornar el resultado de multiplicar los numeros del 1 al 4 

## Con listas:
def mi_funcion():
    lista = []
    for x in range(1,5):
        lista.append(x * 10)
    return lista


## Con generador
def mi_generador():
    for x in range(1,5):
        yield x * 10



print(mi_funcion()) # [10, 20, 30, 40]
print(next(mi_generador())) # 10
print(next(mi_generador())) # 10 imprime siempre el mismo valor porque estoy imprimiendo el resultado de una función
print(next(mi_generador())) # 10
print(next(mi_generador())) # 10
print(next(mi_generador())) # 10
print(type(mi_generador)) # <class 'function'>

# Si deseo iterar el generador debo instanciarlo en una variable previamente: 

mi_generador_instanciado = mi_generador()

print(next(mi_generador_instanciado)) # 10
print(next(mi_generador_instanciado)) # 20
print(next(mi_generador_instanciado)) # 30
print(next(mi_generador_instanciado)) # 40
print(next(mi_generador_instanciado)) # StopIteration

def mi_generador2():
    x = 1
    yield x * 10
    x += 1

print(next(mi_generador2())) # 10
print(next(mi_generador2())) # 10
print(next(mi_generador2())) # 10
print(next(mi_generador2())) # 10
print(next(mi_generador2())) # 10

mi_generador_instanciado2 = mi_generador2()

print(next(mi_generador_instanciado2)) # 10
print(next(mi_generador_instanciado2)) # StopIteration xq no tiene nada más generado para devolver el generador. 
print(next(mi_generador_instanciado2)) # 
print(next(mi_generador_instanciado2)) # 
print(next(mi_generador_instanciado2)) # 

def mi_generador3():
    x = 1
    while True:
        yield x * 10
        x += 1

mi_generador_instanciado3 = mi_generador3()

print(next(mi_generador_instanciado3)) # 10
print(next(mi_generador_instanciado3)) # 20
print(next(mi_generador_instanciado3)) # 30
print(next(mi_generador_instanciado3)) # 40
print(next(mi_generador_instanciado3)) # 50

# Y podría seguir al infinito si quisiera! Esa es la potencia de los generadores. No tienen limites. 
