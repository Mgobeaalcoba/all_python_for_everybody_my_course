class Cubo:
    caras = 6 # Atributo de la clase --> Es compartido por todos los objetos
    def __init__(self, color) -> None: # Atributo de la instancia --> Es propio de cada instancia y puede variar instancia tras instancia
        self.color = color

cubo_1 = Cubo("Amarillo")
cubo_2 = Cubo("Azul")
cubo_3 = Cubo("Naranja")

print(
    f"""
El cubo_1 tiene el atributo caras en {cubo_1.caras} y el atributo colo en {cubo_1.color}
El cubo_2 tiene el atributo caras en {cubo_2.caras} y el atributo colo en {cubo_2.color}
El cubo_3 tiene el atributo caras en {cubo_3.caras} y el atributo colo en {cubo_3.color}
"""
)

"""
El cubo_1 tiene el atributo caras en 6 y el atributo colo en Amarillo
El cubo_2 tiene el atributo caras en 6 y el atributo colo en Azul
El cubo_3 tiene el atributo caras en 6 y el atributo colo en Naranja
"""
