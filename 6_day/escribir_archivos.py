my_file = open("Prueba.txt", "r") # Apertura para lectura
my_file.write("Soy el nuevo texto") # io.UnsupportedOperation: not writable
my_file.close()

# Para poder abrir un archivo para editarlo debo hacerlo en "a" si quiero agregar lineas y "w" si quiero sobreescribir mi archivo. 

my_file = open("Prueba.txt", "a") # Apertura para agregado o creación de uno nuevo
my_file.write("\nSoy el nuevo texto") # io.UnsupportedOperation: not writable
my_file.close()

my_file = open("Prueba1.txt", "a") # Apertura para agregado o creación de uno nuevo
my_file.write("Soy el nuevo texto\n") # io.UnsupportedOperation: not writable
my_file.close()

my_file = open("Prueba1.txt", "w") # Apertura para agregado o creación de uno nuevo
my_file.write("Soy el nuevo texto sobreescrito!!!\n") # io.UnsupportedOperation: not writable
my_file.close()

my_file = open("Prueba2.txt", "w") # Apertura para agregado o creación de uno nuevo
my_file.write("Soy el nuevo texto creado en un file nuevo con el metodo 'w' !!!\n") # io.UnsupportedOperation: not writable
my_file.close()

# Write agrega texto pero no agrega salto de linea automaticamente! 

# Multiples lineas usando literal strings y write:

my_file = open("Prueba2.txt", "w") # Apertura para agregado o creación de uno nuevo
my_file.write("""
Hola
Mundo
Desde
Archivo
""") # io.UnsupportedOperation: not writable
my_file.close()

# Multiples lineas pasando una lista de strings a agregar uno tras otro

my_file = open("Prueba3.txt", "w") # Apertura para agregado o creación de uno nuevo
my_file.writelines(["Hola","Mundo","Desde","Una","Lista"]) # io.UnsupportedOperation: not writable
my_file.close()

# Para agregarle salto de linea podría hacer algo como esto: 

my_file = open("Prueba3.txt", "w")

lista = ["Hola","Mundo","Desde","Una","Lista"]

for palabra in lista:
    my_file.writelines(palabra + "\n")

my_file.close()

