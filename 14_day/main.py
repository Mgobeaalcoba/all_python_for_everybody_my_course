from pathlib import Path
import cv2
import face_recognition as fr
import os

# Loop para revisar mis fotos, codificarlas y comparar la imagen pasada contra las que tengo en la base de datos
## Crear base de datos
ruta = 'Empleados'
mis_imagenes = []
mis_posiciones_de_caras = []
mis_caras_codificadas = []
nombres_empleados = []
lista_empleados = os.listdir(ruta) # Traera los nombres de mis archivos...

# veamos como viene por el momento entonces:
print(lista_empleados) # ['Cosmo Kramer.jpg', 'Elaine Benes.jpg', 'Federico Garay.jpg', 'George Constanza.jpg', 'Jerry Seinfeld.jpg']
print(os.path.basename(lista_empleados[0])) # Cosmo Kramer.jpg

nombre_sin_extension = os.path.splitext(lista_empleados[0])[0]
print(nombre_sin_extension) # Cosmo Kramer

# Directorio actual:
mi_directorio = os.getcwd()
print(mi_directorio)

for empleado in lista_empleados:
    image = fr.load_image_file(Path(ruta, empleado))
    image_modified = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2RGB)

    mis_imagenes.append(image_modified)

    face_place = fr.face_locations(image)[0]

    mis_posiciones_de_caras.append(face_place)

    codified_face = fr.face_encodings(image)[0]

    mis_caras_codificadas.append(image)

print(mis_imagenes)
print(mis_posiciones_de_caras)
print(mis_caras_codificadas)



