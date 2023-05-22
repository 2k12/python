import cv2
import numpy as np

# Cargar la imagen
image = cv2.imread('./pictures/lata1.png')

# Definir las coordenadas del bounding box (ejemplo: x, y, ancho, alto)
x = 100
y = 100
width = 200
height = 150

# Extraer el contenido dentro del bounding box
content = image[y:y+height, x:x+width]

# Convertir el contenido a escala de grises
gray = cv2.cvtColor(content, cv2.COLOR_BGR2GRAY)

# Aplicar umbralización para convertir la imagen en binaria
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Obtener el tamaño del kernel para la operación de dilatación
kernel_size = int(content.shape[1] / 40)

# Definir el kernel estructurante para la operación de dilatación
kernel = np.ones((1, kernel_size), dtype=np.uint8)

# Realizar una operación de dilatación para unir las líneas horizontales
dilated = cv2.dilate(binary, kernel, iterations=1)

# Encontrar los contornos de las líneas dilatadas
contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Extraer las líneas horizontales
horizontal_lines = []
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    aspect_ratio = w / float(h)
    if aspect_ratio > 5:  # Filtrar contornos con un aspecto alargado
        horizontal_lines.append(contour)

# Crear una imagen en blanco del mismo tamaño que el contenido
result = np.zeros_like(content)

# Dibujar las líneas horizontales en la imagen resultante
cv2.drawContours(result, horizontal_lines, -1, (0, 0, 255), thickness=1)

# Mostrar la imagen resultante con las líneas horizontales resaltadas
cv2.imshow('Horizontal Lines', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

