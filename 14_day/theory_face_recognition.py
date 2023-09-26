import cv2
import face_recognition as fr

# Cargar imagenes
foto_control = fr.load_image_file("./images/FotoA.jpg") # Foto Fede 1
foto_prueba = fr.load_image_file("./images/FotoB.jpg") # Foto Fede 2
foto_prueba_2 = fr.load_image_file("./images/FotoC.jpg") # Foto Brad Pitt

# Cambiamos en ambas imagenes la forma en que procesan el color usando cv2:
# Esto se debe a FaceRecognition entiende imagenes que se estructuren en RGB(Red, Green and Blue)
foto_control = cv2.cvtColor(src=foto_control, code=cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(src=foto_prueba, code=cv2.COLOR_BGR2RGB)
foto_prueba_2 = cv2.cvtColor(src=foto_prueba_2, code=cv2.COLOR_BGR2RGB)

# Localizar cara en la foto de control:
lugar_cara_A = fr.face_locations(foto_control)[0] # Siempre es necesario aclarar que estamos enviando el primer elemento de mi imagen con [0]
lugar_cara_B = fr.face_locations(foto_prueba)[0]
lugar_cara_C = fr.face_locations(foto_prueba_2)[0]

# Codificamos la foto:
cara_codificada_A = fr.face_encodings(foto_control)[0]
cara_codificada_B = fr.face_encodings(foto_prueba)[0]
cara_codificada_C = fr.face_encodings(foto_prueba_2)[0]

# Impimo las coordenadas en pixeles de la cara en la foto 1 para entender como armar el rectangulo
print(lugar_cara_A) # (139, 454, 268, 325) puntos de pixeles de la pantalla: alto, derecha, abajo e izquierda respectivamente

# Mostrar rectángulos en la fotos
cv2.rectangle(foto_control,
              (lugar_cara_A[3], lugar_cara_A[0]), # Vértice superior izquierdo
              (lugar_cara_A[1], lugar_cara_A[2]), # Vértice inferior derecho
              (0,255,0), # Color en RGB para el rectángulo
              2) # Grosor del rectángulo

cv2.rectangle(foto_prueba,
              (lugar_cara_B[3], lugar_cara_B[0]),
              (lugar_cara_B[1], lugar_cara_B[2]),
               (0,255,0),
               2)

cv2.rectangle(foto_prueba_2,
              (lugar_cara_C[3], lugar_cara_C[0]),
              (lugar_cara_C[1], lugar_cara_C[2]),
               (0,255,0),
               2)

# Realizar una comparación entre las caras:
## Primero comparo las dos fotos de Fede
resultado = fr.compare_faces([cara_codificada_A], cara_codificada_B) # Si tuviera más de una foto que quiera comparar con la de control, las mismas se sumarían a la lista
## Luego comparo la foto de Fede con la de Brad:
resultado2 = fr.compare_faces([cara_codificada_A], cara_codificada_C)
## Comparo el set completo [Fede, Brad] Vs Fede
resultado3 = fr.compare_faces([cara_codificada_A, cara_codificada_C], cara_codificada_B)

# Imprimo los resultados de mi comparación
print(resultado) # [True] significa que la distancia entre las caras es menor a 0.6 / Así es por default pero se puede modificar si así lo deseamos.
print(resultado2) # [False]
print(resultado3) # [True, False]

# Medida de la distancia:
distancia = fr.face_distance([cara_codificada_A], cara_codificada_B)
distancia2 = fr.face_distance([cara_codificada_A], cara_codificada_C)
distancia3 = fr.face_distance([cara_codificada_A, cara_codificada_C], cara_codificada_B)

# Imprimo ahora las distancias entre los rostros:
print(distancia) # [0.4321014]
print(distancia2) # [0.87577143]
print(distancia3) # [0.4321014  0.87467114]

# Si quiero que me reconozca como la misma persona que Brad Pitt voy a necesitar subir el umbral de 0.6 a 0.88
## Primero comparo las dos fotos de Fede
# resultado = fr.compare_faces([cara_codificada_A], cara_codificada_B, 0.3) # Si tuviera más de una foto que quiera comparar con la de control, las mismas se sumarían a la lista
## Luego comparo la foto de Fede con la de Brad:
# resultado2 = fr.compare_faces([cara_codificada_A], cara_codificada_C, 0.88)
## Comparo el set completo [Fede, Brad] Vs Fede
# resultado3 = fr.compare_faces([cara_codificada_A, cara_codificada_C], cara_codificada_B, 0.6)

# Imprimo los resultados de mi comparación
# print(resultado) # [False] Pese a que las dos fotos son de la misma persona, al bajar el umbral no las reconoce como iguales.
# print(resultado2) # [True] Pese a que una es Fede y la otra es Brad Pitt las reconoce como iguales dado que hemos incrementado el umbral
# print(resultado3) # [True, False] Volviendo al 0.6 por default los valores vuelven a la normalidad.

# Mostrar resultado:
cv2.putText(img=foto_prueba,
            text=f"{resultado} {distancia.round(2)}",
            org=(50, 50),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=1,
            color=(0, 255, 0),
            thickness=2)

# Mostrar imágenes:
cv2.imshow("Foto Control", foto_control)
cv2.imshow("Foto Prueba", foto_prueba) # La mostrará ahora con el resultado configurado arriba:
cv2.imshow("Foto Brad Pitt", foto_prueba_2)

# Mantener el programa abierto:
cv2.waitKey() # Lo mismo que input()

