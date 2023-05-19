# ! Deteccion de Bordes
import cv2


# Cargar la imagen binaria
imagen = cv2.imread('./pictures/captura4.jpg',cv2.IMREAD_GRAYSCALE)

# Aplicar umbralización
umbral, imagen_binaria = cv2.threshold(imagen, 8, 255, cv2.THRESH_BINARY)

# Invertir la imagen binaria
imagen_negativa = cv2.bitwise_not(imagen)

# Aplicar el operador de Canny para detectar los bordes
bordesc = cv2.Canny(imagen_negativa, 100, umbral)

# ! RESTO DE FORMATOS NECESITAN MAS ARGUMENTOS
#bordesc2 = cv2.Sobel(imagen_negativa,100, 0,1)
#bordesc3 = cv2.Laplacian(imagen_negativa)
#bordesc4 = cv2.filter2D(imagen_negativa, 100, 200)




cv2.imshow('Imagen Normal',imagen)
cv2.imshow('Imagen Negativa',imagen_negativa)
cv2.imshow('Canny',bordesc)

cv2.waitKey(0)
cv2.destroyAllWindows()