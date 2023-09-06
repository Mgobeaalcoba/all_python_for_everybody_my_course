# Ejercicio 1: 

class Perro:
    def __init__(self, raza: str, color: str, edad: int) -> None:
        self.raza = raza
        self.color = color
        self.edad = edad
        
    def ladrar(self) -> None:
        print("Guau!")
        
        
pichu = Perro("Calle pero bello", "Amarillo", 2)
pichu.ladrar()

# Ejercicio 2:

class Mago:
    def lanzar_hechizo(self) -> None:
        print("¡Abracadabra!")

merlin = Mago()
merlin.lanzar_hechizo()

# Ejercicio 3:

class Alarma:
    def postergar(self, cantidad_minutos) -> None:
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")