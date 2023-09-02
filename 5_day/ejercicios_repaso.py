# Ejercicio 1:

def devoler_distintos(num1,num2,num3):
    lista = [num1,num2,num3]
    if sum(lista) > 15:
        return max(lista)
    elif sum(lista) < 10:
        return min(lista)
    else:
        print(lista)
        lista.sort()
        print(lista)
        return lista[1]
    
lista = [1,5,10]
print(devoler_distintos(*lista))
lista2 = [2,3,4]
print(devoler_distintos(*lista2))
lista3 = [5,1,7]
print(devoler_distintos(*lista3))


# Ejercicio 2

def devolver_letras(palabra):
    print(palabra)
    my_list = [letra for letra in palabra]
    print(f"primera lista: {my_list}")
    my_set = set(my_list)
    print(f"primer set: {my_set}")
    my_list = list(my_set)
    print(f"segunda lista: {my_list}")
    my_list.sort()
    print(f"lista ordenada: {my_list}")
    return my_list

print(devolver_letras("ornitorrinco"))
