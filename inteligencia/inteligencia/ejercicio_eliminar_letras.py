import cv2
import numpy as np
import matplotlib.pyplot as plt


def eliminarletras():
    imagen = cv2.imread('./pictures/frase.jpg',0)
    _, binary_image = cv2.threshold(imagen, 0, 250, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # Encuentra los contornos en la imagen binaria
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Definir el área mínima deseada para eliminar componentes
    area_threshold = 150
    # Recorrer los contornos y eliminar aquellos con un área menor que el umbral
    filtered_contours = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area >= area_threshold:
            filtered_contours.append(contour)
    # Crear una imagen en blanco del mismo tamaño que la imagen original
    cleaned_image = np.zeros_like(binary_image)
    # Dibujar los contornos filtrados en la imagen en blanco
    cv2.drawContours(cleaned_image, filtered_contours, -1, 255, thickness=cv2.FILLED)
    # Mostrar la imagen resultante
    
    cv2.imshow('binary', binary_image)
    cv2.imshow("Cleaned Image", cleaned_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# eliminarletras()