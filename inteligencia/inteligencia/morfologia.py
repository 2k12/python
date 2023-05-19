import cv2
import numpy as np

# Cargar la imagen en escala de grises
imagen = cv2.imread('./pictures/captura4.jpg', cv2.IMREAD_GRAYSCALE)

# Definir el elemento estructurante (kernel)
kernel = np.ones((5, 5), np.uint8)  # Por ejemplo, un kernel de 5x5 lleno de unos

# Aplicar la dilatación
imagen_dilatada = cv2.dilate(imagen, kernel, iterations=1)

# Aplicar la erosión
imagen_erodida = cv2.erode(imagen, kernel, iterations=1)

# Aplicar la apertura
imagen_apertura = cv2.morphologyEx(imagen, cv2.MORPH_OPEN, kernel)

# Aplicar el cierre
imagen_cierre = cv2.morphologyEx(imagen, cv2.MORPH_CLOSE, kernel)

# Mostrar las imágenes resultantes
cv2.imshow('Imagen original', imagen)
cv2.imshow('Imagen dilatada', imagen_dilatada)
cv2.imshow('Imagen erodida', imagen_erodida)
cv2.imshow('Imagen apertura', imagen_apertura)
cv2.imshow('Imagen cierre', imagen_cierre)
cv2.waitKey(0)
cv2.destroyAllWindows()
