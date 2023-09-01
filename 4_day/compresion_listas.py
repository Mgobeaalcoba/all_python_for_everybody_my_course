# list comprenhension con solo un if
nueva_lista = [num**2 for num in range(10) if num < 5]
print(nueva_lista)

# Esto con un ciclo for sería: 
nueva_lista = []

for i in range(10):
    if i < 5:
        nueva_lista.append(i**2)

print(nueva_lista)

# list comprenhension con if y else: 
nueva_lista = [num**2 if num < 5 else num*10 for num in range(11)]
print(nueva_lista)

# Esto con un ciclo for se haría así:

nueva_lista = []

for i in range(11):
    if i < 5:
        nueva_lista.append(i**2)
    else:
        nueva_lista.append(i*10)

print(nueva_lista)

valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_cuadrado = [valor**2 for valor in valores]

print(valores_cuadrado)

valores = [1, 2, 3, 4, 5, 6, 9.5] 

valores_pares = [valor for valor in valores if valor % 2 == 0]

print(valores_pares)


def conversor(grados):
    return (grados - 32) * (5/9)

temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [conversor(grado) for grado in temperatura_fahrenheit]


