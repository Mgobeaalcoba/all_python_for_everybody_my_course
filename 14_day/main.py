import cv2
import face_recognition as fr

# Cargar imagenes
foto_control = fr.load_image_file("./images/FotoA.jpg")
foto_prueba = fr.load_image_file("./images/FotoB.jpg")

# Cambiamos en ambas imagenes la forma en que procesan el color usando cv2:
# Esto se debe a FaceRecognition entiende imagenes que se estructuren en RGB(Red, Green and Blue)
foto_control = cv2.cvtColor(src=foto_control, code=cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(src=foto_prueba, code=cv2.COLOR_BGR2RGB)

# Localizar cara en la foto de control:
lugar_cara_A = fr.face_locations(foto_control)[0] # Siempre es necesario aclarar que estamos enviando el primer elemento de mi imagen con [0]
lugar_cara_B = fr.face_locations(foto_prueba)[0]

# Codificamos la cara encontrada:
cara_codificada_A = fr.face_encodings(foto_control)[0]
cara_codificada_B = fr.face_encodings(foto_prueba)[0]

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

# Mostrar imágenes:
cv2.imshow("Foto Control", foto_control)
cv2.imshow("Foto Prueba", foto_prueba)

# Mantener el programa abierto:
cv2.waitKey() # Lo mismo que input()

