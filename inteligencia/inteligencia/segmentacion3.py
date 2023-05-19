import cv2

# Cargar la imagen binaria
imagen = cv2.imread('./pictures/captura4.jpg',cv2.IMREAD_GRAYSCALE)
umbral, imagen_binaria = cv2.threshold(imagen, 8, 255, cv2.THRESH_BINARY)

imagen_negativa = cv2.bitwise_not(imagen_binaria)

# Aplicar el etiquetado de componentes
num_componentes, etiquetas = cv2.connectedComponents(imagen_negativa)

# Mostrar el número total de componentes
print('Número total de componentes:', num_componentes)

# Mostrar las etiquetas de los componentes
print('Etiquetas de los componentes:', etiquetas)

# Mostrar las imágenes etiquetadas
cv2.imshow('Imagen binaria', imagen_binaria)
cv2.imshow('Imagen etiquetada', etiquetas.astype('uint8') * (255 // num_componentes))
cv2.waitKey(0)
cv2.destroyAllWindows()