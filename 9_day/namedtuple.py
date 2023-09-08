from collections import namedtuple

mi_tupla = (500, 18, 65)

print(mi_tupla[1]) # 18

# namedtuple nos genera tuplas a las cuales no solo podremos acceder a traves de su indice sino también a traves de su nombre. 

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso']) # Defino a Persona como un objeto namedtuple

# Defino personas
mariano = Persona("Mariano", 175, 90)
ariel = Persona('Ariel', 176, 79)

# Ahora puedo acceder a los elementos de mi tupla usando los nombres dado que fueron nominados --> Es parecido a acceder a los atributos de una clase

print(ariel.altura) # 176
print(mariano.nombre) # Mariano

# Pero sigo pudiendo acceder a sus valores mediante el indice tal como si fuese una tupla comun:

print(ariel[1]) # 176
print(mariano[0]) # Mariano


