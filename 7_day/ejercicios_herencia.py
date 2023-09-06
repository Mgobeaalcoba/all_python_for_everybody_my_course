# Ejercicio 1:

class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
        
class Alumno(Persona):
    pass

# Ejercicio 2:

class Mascota:
    def __init__(self, edad, nombre, cantidad_patas) -> None:
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas
        
class Perro(Mascota):
    pass

# Ejercicio 3: 

class Vehiculo:
    def acelerar(self):
        pass
    
    def frenar(self):
        pass
    
class Automovil(Vehiculo):
    pass