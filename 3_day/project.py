# Esta es una prueba para poder testear el proyecto del día 3 del curso de Python Total

def run():
    text = input("Ingrese por favor el texto a analizar: ")
    letter = input("Ingrese la primera letra que desea buscar en el texto: ")
    letter2 = input("Ingrese la segunda letra que desea buscar en el texto: ")
    letter3 = input("Ingrese la tercera letra que desea buscar en el texto: ")
    text = text.lower()
    letter_repeat = text.count(letter)
    letter2_repeat = text.count(letter2)
    letter3_repeat = text.count(letter3)
    print(f'La letra {letter} se repite {letter_repeat} veces.')
    print(f'La letra {letter2} se repite {letter2_repeat} veces.')
    print(f'La letra {letter3} se repite {letter3_repeat} veces.')

    count_words = len(text.split())
    print(f'El texto tiene {count_words} palabras.')

    first_letter = text[0]
    last_letter = text[-1]
    print(f'La primera letra del texto es: {first_letter}.')
    print(f'La última letra del texto es: {last_letter}.')

    inverse_words = " ".join(text.split()[::-1])
    print(f'Su texto a la inversa se vería así: {inverse_words}.')

    python_in_text = "python" in text
    print(f'Aparece Python en el texto ingresado: {python_in_text}.')

if __name__ == '__main__':
    run()