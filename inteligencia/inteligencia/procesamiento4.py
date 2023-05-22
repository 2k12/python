import cv2
import numpy as np

def main():
    # Cargar la imagen en formato BGR (por defecto de OpenCV)
    imagen_bgr = cv2.imread('./pictures/captura4.jpg')
    
    # Convertir la imagen de BGR a HSV
    imagen_hsv = cv2.cvtColor(imagen_bgr, cv2.COLOR_BGR2HSV)
    
    # Mostrar la imagen original y la imagen en espacio de color HSV
    cv2.imshow('Imagen original', imagen_bgr)
    cv2.imshow('Imagen en espacio de color HSV', imagen_hsv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
