dic = {'c1' : 'a', 'c2': 'b', 'c3': 'c'}

for i in dic:
    print(i + " : " + dic[i])

for i in dic.items():
    print(i)

for clave, valor in dic.items():
    print(clave + " : " + valor)

for clave in dic.keys():
    print(clave)

for valor in dic.values():
    print(valor)

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for nombre in alumnos_clase:
    print(f"Hola {nombre}")

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for numero in lista_numeros:
    suma_numeros += numero  

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero