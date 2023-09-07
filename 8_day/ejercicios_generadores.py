# Ejercicio 1

def mi_generador():
    x = 1
    while True:
        yield x
        x += 1
        
generador = mi_generador()

# Ejercicio 2

def multiplos_de_7():
    x = 7 
    while True:
        yield x 
        x += 7 
        
generador = multiplos_de_7()

# Ejercicio 3

def contador_vidas():
    vidas = 3
    while True:
        if vidas > 1:
            yield f"Te quedan {vidas} vidas"
            vidas -= 1
        elif vidas > 0:
            yield f"Te queda {vidas} vida"
            vidas -=1
        else:
            yield f"Game Over"
            
perder_vida = contador_vidas()

