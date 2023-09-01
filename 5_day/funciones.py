def saludar():
    print("¡Hola mundo!")

def bienvenida(nombre_persona):
    print(f"¡Bienvenido {nombre_persona}!")

nombre_persona = "Mariano"

def cuadrado(un_numero):
    print(un_numero**2)
    
un_numero = 5

def potencia(num1, num2):
    return num1**num2

def usd_a_eur(monto):
    return monto * 0.9
    
dolares = 105

def invertir_palabra(palabra):
    return palabra.upper()[::-1]
    
palabra = "Python"

print(invertir_palabra(palabra))

def todos_positivos(lista):
    for numero in lista:
        if numero < 0:
            return False
    return True
    
lista_numeros = [1,2,3,4,5,7,6,1]
print(todos_positivos(lista_numeros))


def suma_menores(lista_numeros):
    suma_num = 0
    for numero in lista_numeros:
        if numero > 0 and numero < 1000:
            suma_num += numero
    return suma_num

lista_numeros = [1,2,3,4,5,-10,-25,1500,11234]
print(suma_menores(lista_numeros))


from random import randint

def cantidad_pares(lista_numeros):
    count_num = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            count_num += 1 
    return count_num
    
lista_numeros = [randint(1,1000) for i in range(1,10)]

# for i in range(1,10):
#     lista_numeros.append(randint(1,1000))

print(lista_numeros)
print(cantidad_pares(lista_numeros))

from random import randint

def lanzar_dados():
    x, y = randint(1,6), randint(1,6)
    return evaluar_jugada(x,y)
    
def evaluar_jugada(num1, num2):
    suma_dados = num1 + num2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"    

jugada = lanzar_dados()
print(jugada)


from random import randint

def reducir_lista(mi_lista):
    mi_lista = list(set(mi_lista))
    mi_lista.pop(mi_lista.index(max(mi_lista)))
    return mi_lista

def promedio(mi_lista):
    return sum(mi_lista)/len(mi_lista)
    

lista_numeros = [randint(1,100) for i in range(1,100)]
# lista_numeros = [1,2,15,7,2]

print(lista_numeros)
lista_reducida = reducir_lista(lista_numeros)
print(lista_reducida)
print(promedio(lista_reducida))


from random import choice, randint

def lanzar_moneda():
    options = ["Cara","Cruz"]
    return choice(options)
    
def probar_suerte(moneda, lista_numeros):
    if moneda == "Cara":
        print("La lista se autodestruirá")
        return lista_numeros[1:1]
    else:
        print("La lista fue salvada")
        return lista_numeros

tiro_moneda = lanzar_moneda()
lista_numeros = [randint(1,10) for i in range(10)]

resultado = probar_suerte(tiro_moneda,lista_numeros)
print(resultado)
print(type(resultado))