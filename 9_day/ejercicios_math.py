# Ejercicio 1

import math 

resultado = math.log(25,10)
resultado2 = math.log10(25)
print(resultado) # 1.3979400086720375
print(resultado2) # 1.3979400086720377 

# Ejercicio 2

import math

resultado = math.sqrt(math.pi)
print(resultado) # 1.7724538509055159

# Ejercicio 3

import math

resultado = math.factorial(7)
print(resultado) # 5040

def hallar_factorial(numero):
    acumulador = numero
    print(f"Acumulador vale: {acumulador} al inicio")
    for numero2 in range(1, numero):
        acumulador *= numero2
        print(f"Acumulador vale: {acumulador} en el cilo {numero2}")
    return acumulador

resultado2 = hallar_factorial(7)
print(resultado2)

"""
Se han guardado todos los cambios
|
Línea 15, Columna 18
5040
Acumulador vale: 7 al inicio
Acumulador vale: 7 en el cilo 1
Acumulador vale: 14 en el cilo 2
Acumulador vale: 42 en el cilo 3
Acumulador vale: 168 en el cilo 4
Acumulador vale: 840 en el cilo 5
Acumulador vale: 5040 en el cilo 6
5040
"""
