"""
¿Como hacemos si queremos abrir todos los archivos de un determinado directorio? 
¿Como hacemos si queremos mover un archivo de un directorio a otro? 
Todo esto y mucho más puede hacerse con el modulo OS y Shutil
"""

import os
from pathlib import Path

# directorio actual
print(os.getcwd()) # c:\Users\mgobea\Documents\develop\python_totals --> Las back slash me indican que estoy trabajando en Windows! 

# creo un archivo en mi directorio actual
archivo = open("curso.txt", "w")
archivo.write("Texto de prueba")
archivo.close()

# listo todos los archivos y directorios que tengo dentro de mi directorio actual: 

directory_content = os.listdir()
print(directory_content) # ['.git', '.gitignore', '1_day', '2_day', '3_day', '4_day', '5_day', '6_day', '7_day', '8_day', '9_day', 'curso.txt', 'README.md']
home = Path(os.getcwd())

# Quiero obtener ahora un listado filtrado solo de mis archivos y luego uno solo de mis directorios:

archivos_list = list(filter(os.path.isfile, directory_content))
print(archivos_list) # ['.gitignore', 'curso.txt', 'curso_2.txt', 'prueba.json', 'prueba.txt', 'README.md']

directories_list = list(filter(os.path.isdir, directory_content))
print(directories_list) # ['.git', '1_day', '2_day', '3_day', '4_day', '5_day', '6_day', '7_day', '8_day', '9_day']

# Quiero escribir en todos los .txt una linea que diga "Esto es un .txt"

for element in directory_content:
    file = home / element
    if file.suffix == ".txt":
        open_file = open(file, "a+")
        print(open_file.name)
        open_file.write("\nEsto es un .txt")
        open_file.close()
        print(file.read_text())

"""
[Running] python -u "c:\Users\mgobea\Documents\develop\python_total\9_day\os_profundo.py"
c:\Users\mgobea\Documents\develop\python_total
['.git', '.gitignore', '1_day', '2_day', '3_day', '4_day', '5_day', '6_day', '7_day', '8_day', '9_day', 'curso.txt', 'curso_2.txt', 'prueba.json', 'prueba.txt', 'README.md']
c:\Users\mgobea\Documents\develop\python_total\curso.txt
Texto de prueba
Esto es un .txt
c:\Users\mgobea\Documents\develop\python_total\curso_2.txt

Esto es un .txt
Esto es un .txt
Esto es un .txt
Esto es un .txt
c:\Users\mgobea\Documents\develop\python_total\prueba.txt

Esto es un .txt
Esto es un .txt
Esto es un .txt
Esto es un .txt
"""
