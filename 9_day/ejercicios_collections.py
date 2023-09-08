# Ejercicio 1

from collections import Counter

lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

contador = Counter(lista)
print(contador)

"""
Counter({5: 4, 2: 3, 1: 2, 3: 2, 6: 2, 7: 2, 4: 1})
"""

# Ejercicio 2

from collections import defaultdict

mi_diccionario = defaultdict(lambda: 'Valor no hallado')

mi_diccionario["edad"] = 44
print(mi_diccionario["edad"])
print(mi_diccionario["altura"])

"""
44
Valor no hallado
"""

# Ejercicio 3

from collections import deque

mi_lista = ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]

lista_ciudades = deque(mi_lista)

print(mi_lista) # ['Londres', 'Berlin', 'Par�s', 'Madrid', 'Roma', 'Mosc�']
print(lista_ciudades) # deque(['Londres', 'Berlin', 'Par�s', 'Madrid', 'Roma', 'Mosc�'])
print(type(mi_lista)) # <class 'list'>
print(type(lista_ciudades)) # <class 'collections.deque'>

nueva_lista = ["Buenos Aires", "Cordoba", "Rosario"]
nueva_lista_2 = ["Brasilia", "Florianopolis", "Porto Alegre"]

for ciudad in nueva_lista:
    lista_ciudades.appendleft(ciudad)

print(lista_ciudades) # deque(['Rosario', 'Cordoba', 'Buenos Aires', 'Londres', 'Berlin', 'Par�s', 'Madrid', 'Roma', 'Mosc�'])

for ciudad in nueva_lista_2:
    lista_ciudades.append(ciudad)

print(lista_ciudades) # 

lista_ciudades.popleft() 
print(lista_ciudades) # deque(['Cordoba', 'Buenos Aires', 'Londres', 'Berlin', 'Par�s', 'Madrid', 'Roma', 'Mosc�', 'Brasilia', 'Florianopolis', 'Porto Alegre'])
lista_ciudades.pop()
print(lista_ciudades) # deque(['Cordoba', 'Buenos Aires', 'Londres', 'Berlin', 'Par�s', 'Madrid', 'Roma', 'Mosc�', 'Brasilia', 'Florianopolis'])
