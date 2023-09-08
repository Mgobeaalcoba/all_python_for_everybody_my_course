import os
import shutil
import send2trash

# Otros metodos:
# os.unlink(os.getcwd() + "\\1_day\\file_a_mover.txt") # Elimina un archivo en una ruta que yo le provea
# os.rmdir("ruta_de_ejemplo") # Elimina una carpeta VACIA que le pase como parametro
# shutil.rmtree("ruta_de_ejemplo") # DANGER!!! Elimina la carpeta que se pase como parametro con todo lo que la misma tenga dentro. 
# rmtree no envío los archivos eliminados a la papelera sino que los borra directamente. Para enviar a la papelera y poder recuperarlos necesitamos usar send2trash
# que debe ser instalado mediante pip previamente: 
# send2trash.send2trash("archivo_eliminar.txt") # lo enviará a la papelera y se puede recuperar. 

# Recorrer un directorio padre con todos sus hijos e imprimirlos usando os.walk()

ruta = os.getcwd()
print(ruta) # c:\Users\mgobea\Documents\develop\python_total
my_walk = os.walk(ruta)
print(my_walk) # <generator object _walk at 0x0000022B4EB25010>

# Voy a recorrer el generador que tiene todo el contenido de mi ruta actual: 

try:
    while True:
        print(next(my_walk))
except StopIteration:
    print("Iterador vacio!")

"""
[Running] python -u "c:\Users\mgobea\Documents\develop\python_total\9_day\tempCodeRunnerFile.py"
c:\Users\mgobea\Documents\develop\python_total
<generator object _walk at 0x0000015DFDEB5010>
('c:\\Users\\mgobea\\Documents\\develop\\python_total', ['.git', '1_day', '2_day', '3_day', '4_day', '5_day', '6_day', '7_day', '8_day', '9_day'], ['.gitignore', 'curso.txt', 'curso_2.txt', 'prueba.json', 'prueba.txt', 'README.md'])
('c:\\Users\\mgobea\\Documents\\develop\\python_total\\.git', ['hooks', 'info', 'logs', 'objects', 'refs'], ['COMMIT_EDITMSG', 'config', 'description', 'HEAD', 'index'])
('c:\\Users\\mgobea\\Documents\\develop\\python_total\\.git\\hooks', [], ['applypatch-msg.sample', 'commit-msg.sample', 'fsmonitor-watchman.sample', 'post-update.sample', 'pre-applypatch.sample', 'pre-commit.sample', 'pre-merge-commit.sample', 'pre-push.sample', 'pre-rebase.sample', 'pre-receive.sample', 'prepare-commit-msg.sample', 'push-to-checkout.sample', 'update.sample'])
('c:\\Users\\mgobea\\Documents\\develop\\python_total\\.git\\info', [], ['exclude'])
('c:\\Users\\mgobea\\Documents\\develop\\python_total\\.git\\logs', ['refs'], ['HEAD'])
('c:\\Users\\mgobea\\Documents\\develop\\python_total\\.git\\logs\\refs', ['heads', 'remotes'], [])
('c:\\Users\\mgobea\\Documents\\develop\\python_total\\.git\\logs\\refs\\heads', [], ['main'])
('c:\\Users\\mgobea\\Documents\\develop\\python_total\\.git\\logs\\refs\\remotes', ['origin'], [])
('c:\\Users\\mgobea\\Documents\\develop\\python_total\\.git\\logs\\refs\\remotes\\origin', [], ['main'])
...
Iterador vacio!
"""

# Mover un archivo del directoria actual a otro directorio: 

shutil.move('file_a_mover.txt', os.getcwd() + "\\1_day")
if 'file_a_mover.txt' not in os.listdir():
    print("Movimiento de archivo exitoso!")
else:
    print("El movimiento del archivo ha fracasado")


