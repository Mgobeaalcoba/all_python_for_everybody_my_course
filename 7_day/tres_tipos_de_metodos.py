# Los decoradores "@staticmethod" por ejemplo. Nos van a permitir setear distintos tipos de métodos

"""
¿Que pueden hacer los "metodos de instancias"?
1. Acceden y modifican atributos del objeto
2. Acceden a otros métodos
3. Modificar el estado de la clase
"""

# Ejemplo:

class Pajaro:
    alas = True
    def __init__(self, color, especie) -> None:
        self.color = color
        self.especie = especie

    # Métodos de instancias
    def piar(self):
        print("pio")

    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")
        self.piar() # Llama a otro método

    def pintar_negro(self):
        self.color = "negro"
        print(f"Ahora el pajaro es {self.color}")

    # Metodos de clase: En lugar de self (referencia a las instancias) lleva cls como parametro (referencia a la clase en sí):
    @classmethod
    def poner_huevos(cls, cantidad_huevos):
        # No puedo acceder a los atributos de la instancia con un metodo de clase. Si a un atributo de clase como por ejemplo "alas"
        print(f"Puso {cantidad_huevos} huevos")
        cls.alas = False

    # Métodos Estaticos:
    @staticmethod
    def mirar(): # No se refieren ni a la clase ni a las instancias y no pueden modificar atributos de ningun tipo tampoco
        # Su utlidad es asegurar que ciertos métodos no puedan modificar otros atributos u otros métodos de nuestra clase. 
        print("El pajaro está mirando!")

# Uso de la clase Pajaro:

piolin = Pajaro("Amarillo", "Canario")

piolin.piar()
print()
piolin.volar(150)
print()
piolin.pintar_negro()
print(f"El atributo alas de piolin es {piolin.alas}")
print(f"El color de piolin es {piolin.color}")

# Puedo finalmente cambiar un atributo como "alas" que le pertenece a toda la clase así: 

piolin.alas = False

# Si genero un nuevo pajaro y veo su atributo alas voy a ver que el mismo ahora es False

piolin2 = Pajaro("Naranja", "Canario de las Bermudas")
print(f"El atributo alas de piolin es {piolin2.alas}")

# Uso el class method sin necesidad de instanciar ningun objeto Pajaro: 
Pajaro.poner_huevos(13) # Puso 13 huevos

# Uso del static method: Se peuden llamar tanto desde la clase como desde las instancias!!! 
Pajaro.mirar() # El pajaro est� mirando!

piolin.mirar() # El pajaro est� mirando!
