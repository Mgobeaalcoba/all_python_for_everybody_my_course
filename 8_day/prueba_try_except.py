# 2° forma de manejar el ingreso equivocado de un tipo de dato usando try/except

def pedir_numero_2(numero = 0):
    try:
        numero = int(input("Dame un numero: "))
    except ValueError:
        print("Ese no es es un numero! ")
        numero = 0
        pedir_numero_2()
    return numero


numero2 = pedir_numero_2()
print(numero2)

# No funciona dado que el primer retorno debe volver también! 