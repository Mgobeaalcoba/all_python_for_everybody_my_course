from random import *

mi_num = randint(1,10) # Elige un entero entre los rangos informados. 
print(mi_num)

aleatorio = uniform(1,5) # Elige un decimal entre los rangos informados
print(aleatorio)

aleatorio2 = round(uniform(1,5),2)
print(aleatorio2)

aleatorio3 = random() # Elije solo un decimal aleatorio entre 0 y 1
print(aleatorio3)

colores = ["rojo","azul","amarillo","marron"]

aleatorio4 = choice(colores) # Selecciona de forma aleatoria una variante de la colección pasada como parametro. 
print(aleatorio4)

# Shuffle (Mezclar)

numeros = list(range(5,50,5))
print(numeros)

shuffle(numeros) # Mezclara los elementos de mi lista y los presentara con un nuevo orden: 

print(numeros)