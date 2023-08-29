# Dos formas de construir tuples:
mi_tuple = (1,2,3,4) # Forma más común de encontrar las tuplas. 
print(type(mi_tuple))
mi_tuple_2 = 1,2,3,4
print(type(mi_tuple_2))

# Puedo indexar y fraccionar los tuples como una lista o string:
print(mi_tuple_2[1:4])

# No pueden editarse los tuples. 

# Si puedo anidar tuples dentro de tuples. 

# Puedo castear mi tuple a lista para luego editarlo por ejemplo:

mi_tuple_2 = list(mi_tuple_2)
print(type(mi_tuple_2)) # <class 'list'>

# Y a la inversa también: 
mi_tuple_2 = tuple(mi_tuple_2)
print(type(mi_tuple_2)) # <class 'tuple'>

# Puedo reasignar el contenido de mi tuple a distintas variables
t = 1,2,3
x,y,z = t # También funciona con las listas y los diccionarios este "desempacado"

print(x,y,z)
print(t)
print(len(t))

t = 1,2,3,1,1

# Metodos propios de los tuples:
print(t.count(1)) # 3 / El count también sirve para las listas. 

# Ejercicios con tuples: 

"""
Utiliza un método de tuplas para contar la cantidad de veces que aparece el valor 2 en la siguiente tupla, y muestra el resultado (integer) en pantalla:

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
"""

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))

"""
Convierte a lista la siguiente tupla, y almacénala en una variable llamada mi_lista.

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
"""

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)

"""
Extrae los elementos de la siguiente tupla en cuatro variables: a, b, c, d

mi_tupla = (1, 2, 3, 4)
"""

mi_tupla = (1, 2, 3, 4)
a,b,c,d = mi_tupla
