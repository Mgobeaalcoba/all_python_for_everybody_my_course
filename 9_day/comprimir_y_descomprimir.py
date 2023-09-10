import zipfile

mi_zip = zipfile.ZipFile("archivo_comprimido.zip", "w") # Detallo el nombre de mi comprimido y el modo "w" es para poder ponerle el contenido

# Al correr el codigo anterior creo en mi carpeta actual el archivo .zip detallado arriba

mi_zip.write("mi_texto_A.txt") # Detallo el texto que quiero meter dentro de mi carpeta .zip
mi_zip.write("mi_texto_B.txt") # Detallo el segundo texto que quiero meter. 

mi_zip.close() # Cierro el archivo .zip para liberar espacio en memoria. 

# Ahora vamos a descomprimir:

import zipfile

zip_abierto = zipfile.ZipFile("archivo_comprimido.zip", "r") # Solo lectura para extraer el contenido:
zip_abierto.extractall() # Extrae en el directorio actual el contenido de la carpeta .zip

# Otra forma de comprimir es usar "shutil":

import shutil

# voy a comprimir el contenido de mi carpeta "Alternativo" que se encuentra en mi desktop:

carpeta_origen = "C:\\Users\\mgobea\\Desktop\\Alternativo"

archivo_destino = "Alternativo_Comprimido"

shutil.make_archive(archivo_destino, 'zip', carpeta_origen)

# Descomprimir usando "shutil"

import shutil

shutil.unpack_archive("Alternativo_Comprimido.zip", "Extraccion_hecha_con_shutil", 'zip')

