import cv2
import numpy as np


# Definir el tamaño del elemento estructural
size = (100,100)

# Calcular el centro del elemento estructural
center = (size[1] // 2, size[0] // 2)

# Calcular el radio del círculo mediano
radius = min(size) // 2

# Crear una matriz de ceros del tamaño especificado
element = np.zeros(size, dtype=np.uint8)

# Dibujar un círculo mediano en la matriz
cv2.circle(element, center, radius, 1, thickness=-1)

# Mostrar el elemento estructural
cv2.imshow("Elemento Estructural", element)
cv2.waitKey(0)
cv2.destroyAllWindows()