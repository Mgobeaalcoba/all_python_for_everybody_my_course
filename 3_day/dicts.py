diccionario = {
    'c1':'valor1',
    'c2':'valor2',
    'c3':'valor3'
} # Las claves deben ser unicas. Pero los valores pueden ser repetidos. 

print(type(diccionario))
print(diccionario)
print(diccionario['c1']) # Consulto solo un valor del dict

dic = {
    'c1': 55,
    'c2': [100,25]
}

print(type(dic))
print(dic['c2'][1]) # Consulto la lista que está dentro del diccionario. 

# Imprimir del diccionario de abajo la letra 'e' pero en mayuscula

dic = {
    'c1' : ['a','b','c'],
    'c2' : ['d','e','f']
}

print(dic['c2'][1].upper())

# Agregar elementos a un diccionario (dic):
dic['c3'] = ['g','h','i'] # Tmb podría sobreescribir con el mismo contenido una clave ya existente como dic['c2']
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())

# Ejercicios: 

"""
Crea un diccionario llamado mi_dic que almacene la siguiente información de una persona:

nombre: Karen

apellido: Jurgens

edad: 35

ocupacion: Periodista

Los nombres de las claves y valores deben ser iguales a la consigna.
"""

mi_dic = {
'nombre': 'Karen',
'apellido': 'Jurgens',
'edad': 35,
'ocupacion': 'Periodista'
}

"""
Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario.

Si el valor 300 cambiara en el futuro, el código debería funcionar igual para devolver el valor que se encuentre en esa misma posición. Para ello, deberás hacer referencia a los nombres de las claves y/o índices según corresponda.
"""

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])

"""
Actualiza la información de nuestro diccionario llamado mi_dic  (reasignando nuevos valores a las claves según corresponda), y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:

nombre: Karen

apellido: Jurgens

edad: 36

ocupacion: Editora

pais: Colombia

para ello, no debes cambiar la línea de código ya escrita, sino actualizar los valores mediante métodos de diccionarios.
"""

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic['edad'] = 36
mi_dic['ocupacion'] = 'Editora'
mi_dic['pais'] = 'Colombia'
