# Ingresar por consola multiples lineas de texto y mostrarselas al usuario:  

# Inicializa una lista para almacenar las líneas de texto ingresadas por el usuario
lineas_de_texto = []

print("Ingresa múltiples líneas de texto. Presiona Enter en una línea vacía para finalizar.")

while True:
    linea = input()
    
    # Si la línea está vacía, termina el bucle
    if not linea:
        break
    
    # Agrega la línea a la lista
    lineas_de_texto.append(linea)

# Combina las líneas de texto en un solo string (puedes usar '\n' para separarlas)
texto_completo = '\n'.join(lineas_de_texto)



# Imprime el texto completo ingresado por el usuario
print("Texto ingresado por el usuario:")
print(texto_completo)

###
import os

my_file = os.getcwd()
print(my_file)

lineas_de_texto = []

print("Ingrese el contenido de su receta. Presione Enter en una línea vacía para finalizar.")

while True:
    linea = input()

    if not linea:
        break
    
    lineas_de_texto.append(linea)

texto_completo = '\n'.join(lineas_de_texto)

my_file = open("test_escribir_receta.txt", "w")
my_file.write(texto_completo)
my_file.close()

# print("Texto ingresado por el usuario:")
# print(texto_completo)
