from pathlib import Path
import os

base = Path.home()
# C:\Users\mgobea\Documents\develop\python_total\6_day\Recetas
guia = Path(base, "Documents", "develop", "python_total", "6_day", "Recetas", "Carnes")

elementos = os.listdir(guia)
os.chdir(guia)
current_directory = os.getcwd()

print(current_directory)

print("Que categoría de recetas desea seleccionar: ")
for indice, elemento in enumerate(elementos):
    print(f"[{indice + 1}] - {elemento}")
option = int(input("Opcion seleccionada: "))
while option not in range(1,len(elementos)):
    print("Seleccionó una opción NO valida... Vuelva a intentarlo. ")
    option = int(input("Opcion seleccionada: "))

guia = Path("Barcelona", "Sagrada_Familia")
print(guia) # Barcelona\Sagrada_Familia

guia = Path("Barcelona", "Sagrada_Familia.txt")
print(guia) # Barcelona\Sagrada_Familia.txt

# Es una ruta relativa y no absoluta. Puede estar en distintas ubicaciones en nuestro sistema de archivos. 

base = Path.home()
print(base) # C:\Users\mgobea

# Si quiero una ruta absoluta entonces podría hacer esto: 

guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_Familia.txt"))
print(guia) # C:\Users\mgobea\Europa\Espa�a\Barcelona\Sagrada_Familia.txt

guia2 = guia.with_name("La_Pedrera.txt")
print(guia2) # C:\Users\mgobea\Europa\Espa�a\Barcelona\La_Pedrera.txt

print(guia.parent) # Devuelve al padre del path indicado: C:\Users\mgobea\Europa\Espa�a\Barcelona
print(guia.parent.parent) # C:\Users\mgobea\Europa\Espa�a

# Armo estructura de Europa para luego iterar sobre sus archivos TXT: 

# C:\Users\mgobea\Documents\develop\python_total\6_day\Europa

my_path = Path(Path.home(), "Documents", "develop", "python_total", "6_day", "Europa")
print(my_path) # C:\Users\mgobea\Documents\develop\python_total\6_day\Europa

print()
for txt in Path(my_path).glob("**/*.txt"):
    print(txt)

print()
for txt in my_path.glob("**/*.txt"):
    print(txt) # Funciona igual que el de arriba pero con menos complejidad. 

guia = Path("Europa", "España", "Barcelona", "Sagrada_Familia.txt")
en_europa = guia.relative_to(Path("Europa"))
en_espania = guia.relative_to(Path("Europa", "España"))
print(en_europa) # Espa�a\Barcelona\Sagrada_Familia.txt
print(en_espania) # Barcelona\Sagrada_Familia.txt

# Puedo también seleccionar rutas relativas desde un punto en particular. Por ejemplo: python_total y develop

# en_python_total = my_path.relative_to(Path("python_total"))
# en_develop = my_path.relative_to(Path("develop"))

# print(en_python_total)
# print(en_develop)

"""
C:\Users\mgobea\Documents\develop\python_total\6_day\Europa\Consejos.txt
C:\Users\mgobea\Documents\develop\python_total\6_day\Europa\Normativas.txt
C:\Users\mgobea\Documents\develop\python_total\6_day\Europa\Espa�a\Barcelona\La_Pedrera.txt
C:\Users\mgobea\Documents\develop\python_total\6_day\Europa\Espa�a\Barcelona\Sagrada_Familia.txt
C:\Users\mgobea\Documents\develop\python_total\6_day\Europa\Espa�a\Madrid\Museo_Del_Prado.txt
C:\Users\mgobea\Documents\develop\python_total\6_day\Europa\Francia\Paris\Torre_Eiffel.txt

C:\Users\mgobea\Documents\develop\python_total\6_day\Europa\Consejos.txt
C:\Users\mgobea\Documents\develop\python_total\6_day\Europa\Normativas.txt
C:\Users\mgobea\Documents\develop\python_total\6_day\Europa\Espa�a\Barcelona\La_Pedrera.txt
C:\Users\mgobea\Documents\develop\python_total\6_day\Europa\Espa�a\Barcelona\Sagrada_Familia.txt
C:\Users\mgobea\Documents\develop\python_total\6_day\Europa\Espa�a\Madrid\Museo_Del_Prado.txt
C:\Users\mgobea\Documents\develop\python_total\6_day\Europa\Francia\Paris\Torre_Eiffel.txt
"""