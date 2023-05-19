import cv2

# Cargar la imagen en escala de grises
imagen = cv2.imread('./pictures/captura4.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar umbralización
umbral, imagen_binaria = cv2.threshold(imagen, 8, 255, cv2.THRESH_BINARY)

# Invertir la imagen binaria
imagen_negativa = cv2.bitwise_not(imagen_binaria)

num_componentes, etiquetas = cv2.connectedComponents(imagen_negativa)

# Mostrar la imagen binarizada
# Mostrar el número total de componentes
print('Número total de componentes:', num_componentes)
cv2.imshow('Imagen binarizada', imagen_binaria)
cv2.imshow('Imagen negativa', imagen_negativa)
cv2.waitKey(0)
cv2.destroyAllWindows()





