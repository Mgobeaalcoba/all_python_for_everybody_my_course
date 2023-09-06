# Usar Herencia es clave para cumplir con el principio DRY = Don't repeat yourself

class Animal:

    def __init__(self, edad, color) -> None:
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

class Pajaro(Animal):
    pass

class Perro(Animal):
    pass

# Comprobar que la herencia que está instituida: 
print(Pajaro.__bases__) # (<class '__main__.Animal'>,) --> Me muestra que Pajaro hereda de Animal! 

# Comprobar que clases hijas tiene una clase se puede hacer así:
print(Animal.__subclasses__()) # [<class '__main__.Pajaro'>, <class '__main__.Perro'>]

piolin = Pajaro(2, "amarillo")
piolin.nacer() # Este animal ha nacido ---> nacer lo heredo de Animal sin necesidad de que vuelva a duplicar el codigo. 
print(piolin.color + "/" + str(piolin.edad)) # amarillo/2