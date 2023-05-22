import cv2
import numpy as np
import matplotlib.pyplot as plt


def llaves():
    imagen=cv2.imread('./pictures/llaves.png',0)
    imagen_negativa = cv2.bitwise_not(imagen)
    umbral,imagen_binaria= cv2.threshold(imagen_negativa, 0, 255 ,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # * CANNY
    # bordesc = cv2.Canny(imagen_binaria, 100, umbral)
    # * LAPLACIANO
    bordesc2 = cv2.Laplacian(imagen_binaria, cv2.CV_64F)
    # Convertir los valores a enteros sin signo
    bordesc2 = cv2.convertScaleAbs(bordesc2)
    num_componentes, comp = cv2.connectedComponents(bordesc2)
    num_componentes=num_componentes-1
    print('objetos:', num_componentes)
    cv2.imshow('llaves',imagen)
    cv2.imshow('bordes llaves',bordesc2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


llaves()