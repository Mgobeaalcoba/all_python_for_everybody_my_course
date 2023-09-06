# Ejercicio 1:

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
        
    def __str__(self) -> str:
        return '"{self.titulo}", de {self.autor}'

# Ejercicio 2:

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self) -> int:
        return self.cantidad_paginas

# Ejercicio 3:

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self) -> None:
        print("Libro eliminado")