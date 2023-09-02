from random import choice

def run():
    lives = init_game()
    my_word = select_word()
    my_underscores = show_underscores(my_word)
    wrong_letters_list = []

    while not word_complete(my_underscores, my_word) and not no_lives(lives):
        my_letter = request_letter()
        if not valid_letter(my_letter):
            continue
        else:
            if letter_in_word(my_letter, my_word):
                my_underscores = reprint_underscores(my_word, my_letter, my_underscores)
                if word_complete(my_underscores,my_word):
                    end_game(True)
            else:
                
                wrong_letters(my_letter, wrong_letters_list)
                show_wrong_letters(wrong_letters_list)
                lives = subtract_lives(lives)
                show_remaining_lives(lives)
                paint_hanged_man(lives)
                if no_lives(lives):
                    end_game(False)


def init_game():
    lives = 6
    print(f"""
¡Bienvenido al juego del ahorcado!
Usted cuenta con {lives} vidas. 
""")
    return lives


def select_word():
    palabras = [
    "flor", "sol", "casa", "perro", "gato", "lago", "mesa", "silla", "libro", "bola",
    "vino", "tren", "cine", "puerta", "mano", "pie", "nariz", "ojo", "boca", "pelo",
    "dedo", "tierra", "mar", "aire", "nube", "raton", "florero", "nido", "luna", "estrella",
    "plato", "taza", "tetera", "rio", "montana", "bosque", "playa", "ciudad", "parque", "iglesia",
    "colegio", "piscina", "gimnasio", "zapato", "calcetin", "camisa", "pantalon", "abrigo", "sombrero", "guante",
    "bufanda", "cartera", "llave", "reloj", "lapiz", "papel", "puente", "carretera", "avion", "barco",
    "trenza", "collar", "anillo", "pulsera", "reloj", "cama", "almohada", "manta", "espejo", "cepillo",
    "diente", "sabana", "vela", "cuchara"
    ]
    your_word = choice(palabras)
    return your_word


def show_underscores(your_word):
    your_underscores = "_ " * len(your_word)
    print(f"""
Debe adivinar la palabra que se esconde aquí: {your_underscores}
¡Mucha Suerte!
""")
    return your_underscores


def request_letter():
    your_letter = input("Ingrese una letra que crea se encuentra en la palabra a adivinar: ")
    your_letter = your_letter.lower()
    return your_letter


def valid_letter(leter):
    spanish_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    valid = False
    if leter in spanish_letters:
        valid = True
    else:
        print("No ha ingresado una letra válida. Vuelva a intentarlo. ")
    return valid


def letter_in_word(letter, word):
    if letter in word:
        return True
    else:
        return False


def reprint_underscores(your_word, your_letter, your_underscores):
    your_underscores_list = your_underscores.split(" ")
    for i in range(len(your_word)):
        if your_letter == your_word[i]:
            your_underscores_list[i] = your_letter
    your_underscores = " ".join(your_underscores_list)
    print(f"Muy bien!!! Está cerca de adivinar la palabra: {your_underscores} ")
    return your_underscores


def word_complete(your_underscores, your_word):
    your_underscores_list = your_underscores.split(" ")
    your_underscores = "".join(your_underscores_list)
    if your_underscores == your_word:
        return True
    else: 
        return False


def end_game(win_game):
    if win_game:
        print("Felicitaciones! Ha ganado el juego... Vuelva pronto.")
    else:
        print("Se ha quedado sin vidas! No se rinda y vuelva a intentarlo pronto! ")


def wrong_letters(letter, wrong_letters_list):
    if letter not in wrong_letters_list:
        wrong_letters_list.append(letter)


def show_wrong_letters(wrong_letters_list):
    print(f"Las letras incorrectas ingresadas por el momento son: {wrong_letters_list}. ")


def subtract_lives(lives):
    lives -= 1
    return lives


def show_remaining_lives(lives):
    print(f"A usted le quedan {lives} vidas. ")


def paint_hanged_man(lives):
    print ("______")
    print ("|        |")
    if lives == 6:
        print ("|")
        print ("|")
        print ("|")
    elif lives == 5:
        print ("|        O")
        print ("|")
        print ("|")
    elif lives == 4:
        print ("|        O")
        print ("|        |")
        print ("|")
    elif lives == 3:
        print ("|        O")
        print ("|       /|")
        print ("|")
    elif lives == 2:
        print ("|        O")
        print ("|       /|\ ")
        print ("|")
    elif lives == 1:
        print ("|        O")
        print ("|       /|\ ")
        print ("|       / ")
    else:
        print ("|        O")
        print ("|       /|\ ")
        print ("|       / \ ")
    print ("|")
    print ("|___")


def no_lives(lives):
    if lives == 0:
        return True
    else:
        return False
    

if __name__ == '__main__':
    run()
