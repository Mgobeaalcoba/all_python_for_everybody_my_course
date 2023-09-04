# Puede que necesitemos que nuestro programa limpie la pantalla de la consola en determinado momento... 

from os import system

print("Hola Mundo!!!")
system("cls") # clear se debe colocar si el OS es Mac o Linux
print("Chau Mundo!!!")