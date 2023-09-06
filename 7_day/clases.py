
# Clase con un solo atributo que es de tipo "atributo de instancia" y se declara en el constructor __init__
class Pajaro:
    alas = True
    def __init__(self, color, especie) -> None:
        self.color = color
        self.especio = especie


mi_pajaro = Pajaro("Amarillo", "Canario")
mi_pajaro2 = Pajaro("Verde", "Loro")


print(type(mi_pajaro)) # <class '__main__.Pajaro'>
print(mi_pajaro) # <__main__.Pajaro object at 0x0000016AA3791B50>
print(mi_pajaro2) # <__main__.Pajaro object at 0x0000016AA3791B90>

# Ejercicios:
## Ejercicio 1

class Personaje:
    pass

harry_potter = Personaje()

## Ejercicio 2

class Dinosaurio:
    pass

velociraptor = Dinosaurio()
tiranosaurio_rex = Dinosaurio()
braquiosaurio  = Dinosaurio()

## Ejercicio 3: 

class PlataformaStreaming:
    pass

netflix = PlataformaStreaming()
hbo_max = PlataformaStreaming()
amazon_prime_video = PlataformaStreaming()
