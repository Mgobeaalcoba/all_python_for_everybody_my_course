from collections import Counter

numeros = [8,5,6,7,8,5,4,5,6,9,5,6,8,7,9,6,4,7,1,2,3,5,4,1,2,3,6,5]
# Como cuento las repeticiones de los distintos elementos de mi lista?

print(Counter(numeros)) # Counte arma un dict con clave cada elemento de mi lista y valor la cantidad de repeticiones: 

"""
Counter({5: 6, 6: 5, 8: 3, 7: 3, 4: 3, 9: 2, 1: 2, 2: 2, 3: 2})
"""

# Tambien puedo aplicarlo a un string con letras que se repiten:

print(Counter("mississippi")) # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# También podremos contar palabras de una frase como:

print(Counter("Al pan pan y al vino vino")) # Counter({' ': 6, 'n': 4, 'a': 3, 'l': 2, 'p': 2, 'v': 2, 'i': 2, 'o': 2, 'A': 1, 'y': 1})
frase = "Al pan pan y al vino vino"

print(Counter(frase.split())) # Counter({'pan': 2, 'vino': 2, 'Al': 1, 'y': 1, 'al': 1})

serie = Counter([1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,5,5,5,5,6,6,6,6,6,6,6,6,6,6])
print(serie.most_common()) # [(3, 17), (2, 11), (6, 10), (4, 8), (1, 7), (5, 4)] Ordena del más comun o moda al menos común.
print(serie.most_common(1)) # Solo el que mas se repite: [(3, 17)]

