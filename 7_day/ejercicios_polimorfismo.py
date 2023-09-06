# Ejercicio 1:

palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

conjunto = [palabra, lista, tupla]

for elemento in conjunto:
    print(len(elemento))

# Ejercicio 2:

class Mago:
    def atacar(self):
        print("Ataque mágico")

class Arquero:
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai:
    def atacar(self):
        print("Ataque con katana")
        
        
mi_mago = Mago()
mi_arquero = Arquero()
mi_samurai = Samurai()

personajes = [mi_arquero, mi_mago, mi_samurai]


for personaje in personajes:
    personaje.atacar()

# Ejercicio 3:

class Mago:
    def defender(self):
        print("Escudo mágico")

class Arquero:
    def defender(self):
        print("Esconderse")

class Samurai:
    def defender(self):
        print("Bloqueo")
        
# Función que ejecute un método y que reciba un objeto de forma indistinta es una interface en otros
# Lenguajes de Programación com Kotlin o Java

def personaje_defender(personaje):
    personaje.defender()
    
mi_mago = Mago()
mi_arquero = Arquero()
mi_samurai = Samurai()

personaje_defender(mi_mago)
personaje_defender(mi_arquero)
personaje_defender(mi_samurai)

