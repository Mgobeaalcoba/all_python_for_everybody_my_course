class Persona:
    especie = "humano"
    
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad

    def saludar(self) -> None:
        print(f"Hola mi nombre es {self.nombre}")

    def cumplir_anios(self, estado_humor: str) -> None:
        print(f"Cumplir {self.edad + 1} años me pone {estado_humor}")


juan = Persona("Juan", 37)
juan.saludar() # Hola mi nombre es Juan
juan.cumplir_anios("feliz!!!") # Cumplir 38 a�os me pone feliz!!!