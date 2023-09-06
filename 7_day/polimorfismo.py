"""
El polimorfismo es el pilar de la POO mediante el cual un mismo
método puede comportarse de diferentes maneras según el
objeto sobre el cual esté actuando, en función de cómo dicho
método ha sido creado para la clase en particular.

El método len( ) funciona en distintos tipos de objetos: listas, tuplas, strings, entre
otros. Esto se debe a que para Python, lo importante no son los tipos de objetos,
sino lo que pueden hacer: sus métodos
"""

class Perro:
    def hablar(self):
        print("Guau!")


class Gato:
    def hablar(self):
        print("Miau!")


hachiko = Perro()
garfield = Gato()

# Se puede ejecutar sobre disatintos objetos el mismo método usando for loops:

for animal in [hachiko, garfield]:
    animal.hablar()

animales = [hachiko, garfield]

for animal in animales:
    animal.hablar()

# Se puede ejecutar sobre disatintos objetos el mismo método usando functions:

def animal_habla(animal):
    animal.hablar()

animal_habla(hachiko)
animal_habla(garfield)

# Se puede ejecutar sobre disatintos objetos el mismo método usando for loops y funciones de forma conjunta:

def animales_hablan(lista_animales):
    for animal in lista_animales:
        animal.hablar()

animales_hablan(animales)

"""
Guau!
Miau!
Guau!
Miau!
Guau!
Miau!
Guau!
Miau!
"""