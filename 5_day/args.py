def suma(*args):
    print(args) # (2, 3, 4, 5, 56, 7, 7)
    print(type(args)) # <class 'tuple'>
    total = 0
    for numero in args:
        print(type(numero))
        total += numero
    return total

def suma2(*args):
    return sum(args)


print(suma(2,3,4,5,56,7,7))
print(suma(1,2,3))
print(suma(2))
print(suma(1,2,3,4,5,6,7,8,9,10))
print()
print(suma2(2,3,4,5,56,7,7))
print(suma2(1,2,3))
print(suma2(2))
print(suma2(1,2,3,4,5,6,7,8,9,10))


# Ejercicios:

def suma_cuadrados(*args):
    args = list(args)
    for i in range(len(args)):
        args[i] = args[i]**2
    return sum(tuple(args))
    
print(suma_cuadrados(1,2,3))

from random import randint

def suma_absolutos(*args):
    total = 0
    for numero in args:
        if numero < 0:
            total += numero * -1
        else:
            total += numero
    return total
    
lista_numeros = [randint(-10,10) for i in range(randint(5,20))]
print(lista_numeros)
print(suma_absolutos(*lista_numeros))


from random import randint

def numeros_persona(nombre, *args):
    return f'{nombre}, la suma de tus números es {sum(args)}'
    
lista_numeros = [randint(-10,10) for i in range(randint(5,20))]
print(lista_numeros)
print(numeros_persona("Mariano", *lista_numeros))