import cv2
import numpy as np

def eliminacion_caracaters_():
    # Cargar la imagen como una imagen binaria (blanco y negro)
    image = cv2.imread('./pictures/letras.png', 0)  # Reemplaza 'imagen.jpg' con la ruta de tu imagen
    
    # Binarizar la imagen utilizando umbralización
    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    
    # Encontrar los contornos en la imagen binaria
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Crear una imagen en blanco del mismo tamaño que la imagen original
    cleaned_image = np.zeros_like(image)
    
    # Recorrer los contornos y eliminar aquellos con un área menor que el umbral
    for contour in contours:
        area = cv2.contourArea(contour)
        if area >= 150:
            cv2.drawContours(cleaned_image, [contour], -1, 255, thickness=cv2.FILLED)
    
    # Mostrar la imagen resultante
    cv2.imshow("Cleaned Image", cleaned_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


eliminacion_caracaters_()