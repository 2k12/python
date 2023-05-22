import cv2
import matplotlib.pyplot as plt
import numpy as np

def puntaspinon():
    # cargamos la imagen en escala de grises
    imagen = cv2.imread('./pictures/pinon.png',cv2.IMREAD_GRAYSCALE)
    
    imagen_negativa = cv2.bitwise_not(imagen)
    
    #binarizamos la imagen con el metodo otsu
    umbral,imagen_binaria= cv2.threshold(imagen_negativa, 0, 255 ,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    kernel = np.ones((3,3), np.uint8) 
    
    
    # Realizar una operación de dilatación
    dilatada = cv2.dilate(imagen_binaria, kernel, iterations=1)
    
    # Realizar una operación de erosión
    erosionada = cv2.erode(dilatada, kernel, iterations=3)
    
    # Apertura
    imagen_apertura = cv2.morphologyEx(erosionada, cv2.MORPH_OPEN, kernel)
    # Obtener la imagen rellena
    relleno = cv2.subtract(erosionada,imagen_apertura)
    
    num_componentes, comp = cv2.connectedComponents(relleno)
    num_componentes=num_componentes-1
    
    print('puntas:', num_componentes)
    # cv2.imshow('Imagen Normal', imagen)
    cv2.imshow('Imagen nega', imagen_negativa)
    cv2.imshow('Imagen Binaria', imagen_binaria)
    cv2.imshow('Imagen dilatada', dilatada)
    cv2.imshow('Imagen erosionada', erosionada)
    cv2.imshow('Imagen apertura', imagen_apertura)
    cv2.imshow('Imagen Rellena', relleno)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()


