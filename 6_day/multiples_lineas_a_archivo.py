import os

my_list = []

print(len(my_list))

my_directory = os.getcwd()
print(my_directory)

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