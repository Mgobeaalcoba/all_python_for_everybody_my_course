ciudades_habitantes = {"Tijuana":1810645,"León":1579803}
lista_valores = [5**5, 12**2, 3050, 475*2]
print(min(ciudades_habitantes.keys()))
print(max(ciudades_habitantes.values()))
print(max(lista_valores))


lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]

valor_maximo = max(lista_numeros)

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

rango = max(lista_numeros) - min(lista_numeros)

diccionario_edades = {
    "Carlos":55, 
    "María":42, 
    "Mabel":78, 
    "José":44, 
    "Lucas":24, 
    "Rocío":35, 
    "Sebastián":19, 
    "Catalina":2,
    "Darío":49
}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())

print(edad_minima)
print(ultimo_nombre)