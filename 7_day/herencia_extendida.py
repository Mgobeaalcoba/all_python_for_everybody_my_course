class Animal:

    def __init__(self, edad, color) -> None:
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):
    # Dos maneras de agregar atributos a una clase hija
    ## Crear su propio metodo __init__
    """
    def __init__(self, edad, color, altura_vuelo) -> None:
        self.edad = edad
        self.color = color
        self.altura_vuelo = altura_vuelo
    """
    ## La otra forma más pythonica es usar el método super() así:
    def __init__(self, edad, color, altura_vuelo) -> None:
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    # Tres tipos de métodos en función de su relación con la herencia
    ## Los hereados, por ejemplo nacer() tal como está! 
    ## Los heredados y modificados:
    def hablar(self):
        # Sobreescribo su contenido acá:
        print("pio!")
    ## Los métodos nuevos, propios de la clase Pajaro
    def volar(self, metros):
        print(f"El pajaro vuela {metros}")


piolin = Pajaro(2, "amarillo", 300)
piolin.hablar() # pio! --> Porque se sobreescribio el método en la clase Pajaro! 
piolin.volar(120) # El pajaro vuela 120
print(f"La altura de vuelo de Piolin es de {piolin.altura_vuelo}") # La altura de vuelo de Piolin es de 300
