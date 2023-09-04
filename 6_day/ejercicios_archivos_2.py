# 1° Ejercicio

my_file = open("mi_archivo.txt", "w")
my_file.write("Nuevo texto")
my_file.close()

my_file = open("mi_archivo.txt", "r")
print(my_file.readline())
my_file.close()

# 2° Ejercicio

my_file = open("mi_archivo.txt", "a")

new_line = "Nuevo inicio de sesión"

my_file.write(new_line)

my_file.close()

my_file = open("mi_archivo.txt", "r")

print(my_file.read())

my_file.close()

# Ejercicio 3

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
my_file = open("registro.txt", "a")

for palabra in registro_ultima_sesion:
    my_file.writelines(palabra + "\t")

my_file.close()

my_file = open("registro.txt", "r")
print(my_file.read())
my_file.close()