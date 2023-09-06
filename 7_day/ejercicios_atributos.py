# Ejercicio 1:

class Casa:
    def __init__(self, color: str, cantidad_pisos: int) -> None:
        self.color = color
        self.cantidad_pisos = cantidad_pisos
        
casa_blanca = Casa(color = "blanco", cantidad_pisos = 4)

# Ejercio 2:

class Cubo:
    caras = 6 
    def __init__(self, color) -> None: 
        self.color = color
        
cubo_rojo = Cubo("rojo")

# Ejercicio 3:

class Personaje:
    real = False
    def __init__(self, especie: str, magico: bool, edad: int) -> None:
        self.especie = especie
        self.magico = magico
        self.edad = edad
        
harry_potter = Personaje("Humano", True, 17)