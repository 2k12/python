import cv2
import numpy as np


imagen = cv2.imread('./pictures/puntos_lineas_2.PNG')
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)


dx = cv2.Sobel(gris, cv2.CV_64F, 1, 0, ksize=3)
dy = cv2.Sobel(gris, cv2.CV_64F, 0, 1, ksize=3)
bordes = np.sqrt(dx**2 + dy**2).astype(np.uint8)

umbral_min = 100  # Ajusta este valor según tus necesidades
_, binaria = cv2.threshold(bordes, umbral_min, 255, cv2.THRESH_BINARY)

elemento_estructural = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))  # Ajusta el tamaño según tus necesidades
binaria_dilatada = cv2.dilate(binaria, elemento_estructural, iterations=1)

_, etiquetas = cv2.connectedComponents(binaria_dilatada)

objetos = np.unique(etiquetas)[1:]  # Excluye la etiqueta de fondo (0)
for etiqueta in objetos:
    mascara = np.where(etiquetas == etiqueta, 255, 0).astype(np.uint8)
    contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contorno in contornos:
        (x, y, w, h) = cv2.boundingRect(contorno)
        cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 0), 1)


cv2.imshow('Resultado', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()