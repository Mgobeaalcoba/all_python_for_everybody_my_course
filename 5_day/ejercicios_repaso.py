# Ejercicio 1:

def devoler_distintos(num1,num2,num3):
    lista = [num1,num2,num3]
    if sum(lista) > 15:
        return max(lista)
    elif sum(lista) < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]
    
lista = [1,5,10]
print(devoler_distintos(*lista))
lista2 = [2,3,4]
print(devoler_distintos(*lista2))
lista3 = [5,1,7]
print(devoler_distintos(*lista3))


# Ejercicio 2

def devolver_letras(palabra):
    my_list = [letra for letra in palabra]
    my_set = set(my_list)
    my_list = list(my_set)
    my_list.sort()
    return my_list

print(devolver_letras("ornitorrinco"))

# Ejercicio 3

from random import randint

def doble_cero(*args):
    match = False
    for i in range(len(args)-1):
        if args[i] == 0 and args[i+1] == 0:
            match = True
            break
    return match

my_list = [randint(0,5) for i in range(randint(5,20))]
print(my_list)
print(doble_cero(*my_list))

# Ejercicio 4

from random import randint

def contar_primos(numero):
    primos = []
    it_is_prime = True
    for num in range(2,numero):
        for num2 in range(2,num):
            if num % num2 == 0 and num != num2:
                it_is_prime = False
                break
        if it_is_prime == True:
            primos.append(num)
        it_is_prime = True
    return len(primos), primos

my_num = randint(2,100)
print(f"El numero a enviar a la funcion es: {my_num}. ")
count_primos, list_primos = contar_primos(my_num)
print(count_primos)
print(list_primos)        


