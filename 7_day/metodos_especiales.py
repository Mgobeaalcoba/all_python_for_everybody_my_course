class CD:
    def __init__(self, autor, titulo, canciones) -> None:
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self) -> str:
        return f"Banda: {self.autor}, Titulo: {self.titulo}, Cant de canciones: {self.canciones}"
    
    def __len__(self) -> int:
        return self.canciones
    
    def __del__(self) -> None:
        print("Se ha elimindo el cd")

mi_cd = CD('Pink Floyd', 'The Wall', 24)

print(mi_cd) # <__main__.CD object at 0x000002C1C5C220D0>

# Al imprimir mi album me imprime el espacio en memoria. ¿Como hago para que me imprima info sobre mi album en lugar de ello? 
# Sobreescribiendo el metodo especial __str__ dentro de la class CD. A por ello

print(mi_cd) # Al volver a imprimir luego de sobreescribir __str__ el resultado es: Banda: Pink Floyd, Titulo: The Wall, Cant de canciones: 24
print(len(mi_cd)) # Aplica el metodo especial __len__ que fue sobreescrito arriba: 24

# Otra función de Python es del que elimina un objeto almacenado en una variable. Pero por default no hace nada más. Puedo sobreescribir __del__ para que informe de la eliminación al usuario 
del mi_cd