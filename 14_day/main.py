import cv2
import face_recognition as fr

# Cargar imagenes
foto_control = fr.load_image_file("./images/FotoA.jpg")
foto_prueba = fr.load_image_file("./images/FotoB.jpg")

# Cambiamos en ambas imagenes la forma en que procesan el color usando cv2:
# Esto se debe a FaceRecognition entiende imagenes que se estructuren en RGB(Red, Green and Blue)
foto_control = cv2.cvtColor(src=foto_control, code=cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(src=foto_prueba, code=cv2.COLOR_BGR2RGB)

# Mostrar imagenes:
cv2.imshow("Foto Control", foto_control)
cv2.imshow("Foto Prueba", foto_prueba)

# Mantener el programa abierto:
cv2.waitKey() # Lo mismo que input()
