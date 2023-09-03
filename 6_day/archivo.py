my_file = open('Prueba.txt', "r")
print(type(my_file))
print(my_file)

print(my_file.readline()) # Soy la primera linea
print(my_file.readline()) # �Vaya! �Yo soy la segunda!
print(my_file.readline()) # He quedado tercera
print(my_file.readline() + "4") # 4
print(my_file.readline() + "5") # 5
print(my_file.readline() + "6") # 6

my_file.close() # Buena práctica trbajando con archivos dado que libera el espacio en memoria que consume la lectura del archivo. 

# Las ultimas 3 ya no imprimen nada dado que se han vaciado. 

my_file = open('Prueba.txt', "r")
print(type(my_file))
print(my_file)

print(my_file.readlines()) # ['Soy la primera linea\n', '�Vaya! �Yo soy la segunda!\n', 'He quedado tercera']
print(my_file.readlines()) # [] Lista vacia dado que se vació en su impresión anterior. 

my_file.close()

# Recorrer el file con un ciclo. 

my_file = open('Prueba.txt', "r")
print(type(my_file))
print(my_file)

for linea in my_file:
    print(linea)

"""
Soy la primera linea

�Vaya! �Yo soy la segunda!

He quedado tercera
"""

for linea in my_file:
    print(linea)

"""

"""

# La segunda vez ya no imprime nada dado que se ha vaciado el archivo. 

my_file.close()

# Usar read():

my_file = open('Prueba.txt', "r")
print(type(my_file))
print(my_file)

print(my_file.read()) # ['Soy la primera linea\n', '�Vaya! �Yo soy la segunda!\n', 'He quedado tercera']
"""
Soy la primera linea
�Vaya! �Yo soy la segunda!
He quedado tercera
""" # Imprimio el archivo as is sin sumarle renglones adicionales como readline o el ciclo for.

print(my_file.read()) # [] Lista vacia dado que se vació en su impresión anterior. 
"""

""" # No imprimió nada dado que la lista ya estaba vacia. 

my_file.close()

# Guardar las lineas del archivo en una lista para no perderlas frente al vacio: 

my_file = open('Prueba.txt', "r")
print(type(my_file))
print(my_file)

my_lines = []
for linea in my_file:
    my_lines.append(linea)

print(my_lines) # ['Soy la primera linea\n', '�Vaya! �Yo soy la segunda!\n', 'He quedado tercera']

for linea in my_lines:
    print(linea)

"""
Soy la primera linea

�Vaya! �Yo soy la segunda!

He quedado tercera
"""

for linea in my_lines:
    print(linea)

"""
Soy la primera linea

�Vaya! �Yo soy la segunda!

He quedado tercera
"""

for linea in my_lines:
    print(linea)

"""
Soy la primera linea

�Vaya! �Yo soy la segunda!

He quedado tercera
"""

my_file.close()





