import cv2
import numpy as np
import matplotlib.pyplot as plt


def ejercicio_clavos():
    # ? carga de imagenes y conversiones
    imagen = cv2.imread('./pictures/clavos.png',0)
    imagen_negativa = cv2.bitwise_not(imagen)
    _,imagen_binaria = cv2.threshold(imagen_negativa, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # ? obtener bordes de las imagenes
    # * DETECCION DE BORDES USANDO CANNY
    # bordes = cv2.Canny(imagen_binaria,100,umbral)
    # * LAPLACIANO
    bordes = cv2.Laplacian(imagen_binaria, cv2.CV_64F)
    # Convertir los valores a enteros sin signo
    bordes = cv2.convertScaleAbs(bordes)

    # ? genera numero de componenetes
    num_componentes, comp = cv2.connectedComponents(bordes)
    num_componentes = num_componentes -1

    # ?imprime y muestra imagenes
    print('numero de clavos: ',num_componentes)
    cv2.imshow('Imagen etiquetada', comp.astype('uint8') * (255 // num_componentes))
    cv2.imshow('Negativo',imagen_negativa)
    cv2.imshow('Ejercicio Clavos',bordes)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


ejercicio_clavos()