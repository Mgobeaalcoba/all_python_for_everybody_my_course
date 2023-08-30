# zip() combina los elementos de dos listas armando una lista de tuplas que combinan dentro de cada tupla un elemento de cada lista combinada. El largo de la lista de tuplas será igual al largo de la lista más corta combinada

letras = ['w','x','c']
numeros = [50, 65, 90, 110, 135]

for letra, num in zip(letras, numeros):
    print(f'Letra: {letra}, y Número: {num}')

"""
Output: 

Letra: w, y N�mero: 50
Letra: x, y N�mero: 65
Letra: c, y N�mero: 90
"""

print(zip(letras,numeros))

"""
Output:

<zip object at 0x0000028054021340>

Es un zip object pero se vería algo así como: [("w",50),("x",65),("c",90)]
"""

# Para poder verlo debemos castearlo dentro de una lista: 

print(list(zip(letras,numeros))) # [('w', 50), ('x', 65), ('c', 90)]

# Zip puede usarse tanto para dos listas como para tres o más listas. No hay limites: 

ciudades = ["Lima","Buenos Aires","San Pablo"]

print(list(zip(letras, numeros, ciudades)))

for letra, numero, ciudad in zip(letras,numeros,ciudades):
    print(f"letra: {letra}, numero: {numero} y ciudad: {ciudad}")


capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

for pais, capital in zip(paises, capitales):
    print(f"La capital de {pais} es {capital}")

marcas = ["Toddy", "Coca-Cola","La Serenisima", "Disney"]
productos = ["Cookies", "Gaseosa Cola", "Postresito", "On demand platform"]
mi_zip = zip(marcas,productos)

dict_nums = {
    1 : ["uno","um","one"],
    2 : ["dos","dois","two"],
    3 : ["tres","três","three"],
    4 : ["cuatro","quatro","four"],
    5 : ["cinco","cinco","five"]
}

numeros = list(zip(dict_nums[1],dict_nums[2],dict_nums[3],dict_nums[4],dict_nums[5]))
print(numeros)

dict_nums = {
    "espanol" : ["uno","dos","tres","cuatro","cinco"],
    "portugues" : ["um","dois","três","quatro","cinco"],
    "ingles" : ["one","two","three","four","five"]
}

numeros = list(zip(dict_nums["espanol"],dict_nums["portugues"],dict_nums["ingles"]))
print(numeros)