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
    return list(set(palabra.split(""))).sort()

print(devolver_letras("ornitorrinco"))
