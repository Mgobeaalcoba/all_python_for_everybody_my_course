from pathlib import Path, PureWindowsPath

carpeta = Path("C:/Users/mgobea/Desktop/Alternativo") # Para trabajar con paths agnosticos cambio las barras invertidas de windows por barras normales. 
archivo = carpeta / "Otro_archivo.txt" # Forma de concatenar rutas usando objetos Path.

# Al crear la ruta desde Path permito que cualquier sistema que abra este archivo lo pueda entender, ya sea que usa Windows, o Mac o Linux. 

my_file = open(archivo,"r")
print(my_file.read())

"""
Un archivo
Alternativo
para trabajar 
con OS y Path
"""

# Esta es la forma correcta de trabajar con directorios de forma profesional. 

# El objeto Path tiene sus propios métodos que nos permiten a nosotros leer un archivo y hacer otras cosas más directamente desde Path: 

print(archivo.read_text())
"""
Un archivo
Alternativo
para trabajar 
con OS y Path
"""
# No necesitamos abrir ni cerrar nuestro archivo para leerlo. Es mucho más eficiente. 

print(archivo.name) # Otro_archivo.txt
print(archivo.suffix) # .txt
print(archivo.stem) # Otro_archivo
print(archivo.stat()) # os.stat_result(st_mode=33206, st_ino=22799473113893594, st_dev=1681946503, st_nlink=1, st_uid=0, st_gid=0, st_size=54, st_atime=1693838270, st_mtime=1693836355, st_ctime=1693836318)
print(archivo.absolute()) # C:\Users\mgobea\Desktop\Alternativo\Otro_archivo.txt
print(archivo.exists()) # True

if not archivo.exists():
    print("Este archivo no existe!")
else:
    print("Archivo existente!!!")

ruta_windows = PureWindowsPath(archivo)
print(ruta_windows) # C:\Users\mgobea\Desktop\Alternativo\Otro_archivo.txt
