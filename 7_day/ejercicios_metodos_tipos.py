# Ejercicio 1: 

class Mascota:
    @staticmethod
    def respirar() -> None:
        print("Inhalar... Exhalar")

# Ejercicio 2:

class Jugador:
    vivo = False
    @classmethod
    def revivir(cls) -> None:
        cls.vivo = True


# Ejercicio 3:

class Personaje:
    def __init__(self, cantidad_flechas) -> None:
        self.cantidad_flechas = cantidad_flechas
        
    def lanzar_flecha(self):
        self.cantidad_flechas -= 1

