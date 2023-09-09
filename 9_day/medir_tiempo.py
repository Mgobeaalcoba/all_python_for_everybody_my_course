# Time y Timeit para medir tiempos y buscar, por ejemplo, que código es más eficiente

def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

# ¿Cual de las dos ejecuciones para obtener lo mismo es más eficiente/rapida?

import time, timeit

# Forma propia de validación: 

inicio = time.time()
print(prueba_for(15))
fin = time.time()
tiempo_for = fin - inicio
print(f"Demoró {tiempo_for}!")
inicio = time.time()
print(prueba_while(15))
fin = time.time()
tiempo_while = fin - inicio
print(f"Demoró {tiempo_while}!")
if tiempo_while < tiempo_for:
    print("While es más rapido que for!")
elif tiempo_for < tiempo_while:
    print("For es mas rapido que while!")
else:
    print("Ambos son iguales!!!")

"""
Output: 

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Demoró 5.364418029785156e-05!
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Demoró 2.8848648071289062e-05!
While es más rapido que for!
"""

# Otra forma de validación con time:

inicio = time.time()
prueba_for(1000000)
final = time.time()
tiempo_for = final - inicio
print(final - inicio) 

inicio2 = time.time()
prueba_while(1000000)
final2 = time.time()
tiempo_while = final2 - inicio2
print(final2 - inicio2) 

if tiempo_while < tiempo_for:
    print("While es más rapido que for!")
elif tiempo_for < tiempo_while:
    print("For es mas rapido que while!")
else:
    print("Ambos son iguales!!!")

"""
12:59:36 👽 with 🤖 mgobea 🐶 in python/python_total/9_day via 9_day …
➜ python3 medir_tiempo.py
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Demoró 5.984306335449219e-05!
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Demoró 6.198883056640625e-06!
While es más rapido que for!
0.0663301944732666
0.08041906356811523
For es mas rapido que while!    
"""

# Medir usando timeit para procesos muy cortos: 

declaracion = """
prueba_for(10)
"""

mi_setup = """
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
"""

tiempo_for = timeit.timeit(declaracion, mi_setup, number = 100000) # Number establece cuantas veces timeit debe ejecutar el código para comparar su performance

print(f"La duración de tiempo_for por timeit es de: {tiempo_for}")

declaracion2 = """
prueba_while(10)
"""

mi_setup2 = """
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
"""

tiempo_while = timeit.timeit(declaracion2, mi_setup2, number = 100000) # Number establece cuantas veces timeit debe ejecutar el código para comparar su performance

print(f"La duración de tiempo_while por timeit es de: {tiempo_while}")

if tiempo_while < tiempo_for:
    print("While es más rapido que for!")
elif tiempo_for < tiempo_while:
    print("For es mas rapido que while!")
else:
    print("Ambos son iguales!!!")

"""
13:08:38 👽 with 🤖 mgobea 🐶 in python/python_total/9_day via 9_day …
➜ python3 medir_tiempo.py
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Demoró 3.9577484130859375e-05!
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Demoró 6.67572021484375e-06!
While es más rapido que for!
0.0772395133972168
0.11360716819763184
For es mas rapido que while!
La duración de tiempo_for por timeit es de: 0.052399800000785035
La duración de tiempo_while por timeit es de: 0.0686182990002635
For es mas rapido que while!
"""
