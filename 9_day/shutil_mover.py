import os
import shutil
import send2trash

# Otros metodos:
# os.unlink(os.getcwd() + "\\1_day\\file_a_mover.txt") # Elimina un archivo en una ruta que yo le provea
# os.rmdir("ruta_de_ejemplo") # Elimina una carpeta VACIA que le pase como parametro
# shutil.rmtree("ruta_de_ejemplo") # DANGER!!! Elimina la carpeta que se pase como parametro con todo lo que la misma tenga dentro. 
# rmtree no envío los archivos eliminados a la papelera sino que los borra directamente. Para enviar a la papelera y poder recuperarlos necesitamos usar send2trash
# que debe ser instalado mediante pip previamente: 
send2trash.send2trash("archivo_eliminar.txt") # lo enviará a la papelera y se puede recuperar. 


shutil.move('file_a_mover.txt', os.getcwd() + "\\1_day")
if 'file_a_mover.txt' not in os.listdir():
    print("Movimiento de archivo exitoso!")
else:
    print("El movimiento del archivo ha fracasado")


