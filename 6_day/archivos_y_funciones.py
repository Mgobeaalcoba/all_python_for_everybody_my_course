# Podemos crear funciones encargadas de abrir archivos en modo lectura, otras de hacerlo en modo escritura, otra de eliminar archivos, etc

# Ejercicio 1

def abrir_leer(archivo):
    my_file = open(archivo, "r")
    content = my_file.read()
    my_file.close()
    return content
    
lectura_1 = abrir_leer("Prueba.txt")
print(lectura_1)

# Ejercicio 2

def sobrescribir(archivo):
    my_file = open(archivo, "w")
    my_file.write("contenido eliminado")
    my_file.close()

sobrescribir("ejemplo.txt")
my_file = open("ejemplo.txt", "r")
content = my_file.read()
my_file.close()

print(content)

# Ejercicio 3

def registro_error(archivo):
    my_file = open(archivo, "a")
    my_file.write("se ha registrado un error de ejecución")
    my_file.close()
    
# registro_error("log_errores.txt")
# my_file = open("log_errores.txt", "r")
# content = my_file.read()
# my_file.close()

# print(content)
