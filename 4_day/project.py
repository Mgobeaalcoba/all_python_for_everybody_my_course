from random import randint

def run():

    nombre = input("¿Cual es su nombre? ")
    intentos = 8
    acerto = False
    numero = randint(1,100)
    print(f"Bueno, {nombre}, he pensado u número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número. ")
    
    while not acerto and intentos > 0:
        numero_escogido = int(input("¿De que número crees que se trata? "))
        if numero_escogido < 1 or numero_escogido > 100:
            print("Ha elegido un número que no está permitido. ")
        elif numero_escogido < numero:
            print("Su respuesta es incorrecta. Ha elegido un número MENOR al número secreto. ")
            intentos -= 1
        elif numero_escogido > numero:
            print("Su respuesta es incorrecta. Ha elegido un número MAYOR al número secreto. ")
            intentos -= 1
        else:
            print(f"Has ganado. Su número seleccionado es {numero_escogido} y el número que había pensado era {numero}. ")
            acerto = True

    if intentos == 0:
        print(f"{nombre} lo siento pero ya no te quedan más intentos... Vuelve a intentarlo luego. ")

if __name__ == '__main__':
    run()