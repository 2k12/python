import cv2
import numpy as np

# Cargar la imagen en color
imagen_color = cv2.imread('./pictures/captura4.jpg')

# Convertir la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2GRAY)

# Mostrar la imagen en escala de grises
cv2.imshow('Imagen en escala de grises', imagen_gris)
cv2.waitKey(0)
cv2.destroyAllWindows()