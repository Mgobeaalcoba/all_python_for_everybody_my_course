from pathlib import Path
from datetime import datetime
import cv2
import face_recognition as fr
import os

# Loop para revisar mis fotos, codificarlas y comparar la imagen pasada contra las que tengo en la base de datos
ruta = 'Empleados'
mis_imagenes = []
mis_imagenes_modificadas = []
mis_posiciones_de_caras = []
mis_caras_codificadas = [] # lista que importa
nombres_empleados = []
lista_empleados = os.listdir(ruta) # Traera los nombres de mis archivos...

def registrar_ingresos(persona):
    # Guardamos en un csv los registros con sus horarios
    with open("registro.csv", "r+") as f: # Modo de lectura extra que permite insertar
        datos = f.readlines()
        nombres_registro = []
        for linea in datos:
            ingreso = linea.split(",")
            nombres_registro.append(ingreso[0]) # Agrego los nombres a mi lista

        if persona not in nombres_registro:
            ahora = datetime.now()
            string_ahora = ahora.strftime('%H:%M:%S') # Formato de hora para registrar
            f.writelines(f'\n{persona},{string_ahora}')


for empleado in lista_empleados:

    # 1° solución posible para traer la imagen
    image = fr.load_image_file(Path(ruta, empleado))
    # agrego la imagen a mi lista tal como está:
    mis_imagenes.append(image)

    # modifico mi imagen al formato que luego fr puede leer:
    image_modified = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2RGB)
    # agrego mi imagen modificada a mi lista de imagenes modificadas
    mis_imagenes_modificadas.append(image_modified)

    # encuento la ubicación del rostro en la imagen
    face_place = fr.face_locations(image)[0]
    # agrego la posición del rostro a mi lista para tales fines
    mis_posiciones_de_caras.append(face_place)

    # codifico la imagen:
    codified_face = fr.face_encodings(image)[0]
    # agrego la cara modificada a mi lista para tales fines
    mis_caras_codificadas.append(codified_face)

    # extraigo el nombre de mi empleado
    employee_name = Path(empleado).stem
    # agrego los nombres a una lista para ello:
    nombres_empleados.append(employee_name)

# tomar una imagen desde mi camara web:
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW) # toma la foto y la guarda

# # leer la imagen de la camara
exito, imagen = captura.read()
#
if not exito:
    print("No se ha podido tomar la captura")
else:
    # reconocer una cara en esa captura:
    posicion_cara = fr.face_locations(imagen)

    # codificar la cara que ha capturado:
    cara_codificada = fr.face_encodings(imagen)

    # buscar coincidencias con mi base de datos sin loop:
    # ojo con cara_codificada, dado que si bien es una cara está dentro de una lista por eso hay que desempacarla para pasarla como argumento de comparación:
    coincidencias = fr.compare_faces(mis_caras_codificadas, cara_codificada[0])

    # ahora guardo las distancias:
    distancias = fr.face_distance(mis_caras_codificadas, cara_codificada[0])

    indice_coincidencia = None

    for i in range(len(coincidencias)):
        try:
            if coincidencias[i] == True:
                indice_coincidencia = i
        except:
            print("No hay coincidencias")

    try:
        print(posicion_cara)
        # Mostrar nombre del empleado
        nombre = nombres_empleados[indice_coincidencia]

        # Registro el ingreso en mi csv.
        if nombre:
            registrar_ingresos(nombre)

        print(nombre)

        # Dibujar los rectangulos en las imagenes a mostrar
        cv2.rectangle(mis_imagenes[indice_coincidencia],
                      (mis_posiciones_de_caras[indice_coincidencia][3], mis_posiciones_de_caras[indice_coincidencia][0]),  # Vértice superior izquierdo
                      (mis_posiciones_de_caras[indice_coincidencia][1], mis_posiciones_de_caras[indice_coincidencia][2]),  # Vértice inferior derecho
                      (0, 255, 0),  # Color en RGB para el rectángulo
                      2)  # Grosor del rectángulo

        cv2.rectangle(imagen,
                      (posicion_cara[0][3], posicion_cara[0][0]),  # Vértice superior izquierdo
                      (posicion_cara[0][1], posicion_cara[0][2]),  # Vértice inferior derecho
                      (0, 255, 0),  # Color en RGB para el rectángulo
                      2)  # Grosor del rectángulo

        # Mostrar resultado:
        cv2.putText(img=mis_imagenes[indice_coincidencia],
                    text=f"{coincidencias[indice_coincidencia]} {distancias[indice_coincidencia]}",
                    org=(50, 50),
                    fontFace=cv2.FONT_HERSHEY_COMPLEX,
                    fontScale=1,
                    color=(0, 255, 0),
                    thickness=2)

        # Mostrar resultado:
        cv2.putText(img=imagen,
                    text=f"{coincidencias[indice_coincidencia]} {distancias[indice_coincidencia]}",
                    org=(50, 50),
                    fontFace=cv2.FONT_HERSHEY_COMPLEX,
                    fontScale=1,
                    color=(0, 255, 0),
                    thickness=2)

        # Mostrar imágenes:
        cv2.imshow("Foto Base de datos", mis_imagenes[indice_coincidencia])
        cv2.imshow("Foto Control", imagen)

        # Mantener el programa abierto:
        cv2.waitKey()  # Lo mismo que input()
    except:
        print("No se han encontrado coincidencias en nuestra base de datos")






