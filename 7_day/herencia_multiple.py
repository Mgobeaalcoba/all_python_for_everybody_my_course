class Padre:
    def hablar(self):
        print("Hola!")


class Madre:
    def hablar(self):
        print("Buen día!!!")

    def reir(self):
        print("Jajaja!")


class Hijo(Padre, Madre): # La primer herencia prima sobre la segunda
    pass


class Hijo2(Madre, Padre):
    pass


class Nieto(Hijo): # Herencia de generación en generación
    pass


mi_nieto = Nieto()
mi_nieto.hablar() # Hola! --> Hereda de 2 generaciones arriba! 
mi_nieto.reir() # Jajaja! ---> Heredado de Hijo que a la vez heredó de Madre y Padre

mi_hijo = Hijo()
mi_hijo.hablar() # Hola! --> Prima la herencia del Padre por estar a la izquierda

mi_hijo2 = Hijo2()
mi_hijo2.hablar() # Buen d�a!!! --> Prima la herencia de la Madre por estar a la izquierda

# Para conocer el orden de secuencia de busqueda de la herencia de una clase puedo hacer esto: 

print(Nieto.__mro__) # (<class '__main__.Nieto'>, <class '__main__.Hijo'>, <class '__main__.Padre'>, <class '__main__.Madre'>, <class 'object'>)