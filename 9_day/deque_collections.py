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
