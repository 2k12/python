import cv2 
import numpy as np
import matplotlib.pyplot as plt

def eliminarletras():
    imagen = cv2.imread('./pictures/letras.png',0)
    # _,imagen_binaria = cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY, cv2.THRESH_OTSU)
    contornos, _ = cv2.findContours(imagen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    area_minima = 150  # Área mínima deseada
    contornos_filtrados = []

    for contorno in contornos:
        area = cv2.contourArea(contorno)
        if area > area_minima:
            contornos_filtrados.append(contorno)


    imagen_contornos = np.zeros_like(imagen)
    imagen_n = cv2.drawContours(imagen_contornos, contornos_filtrados, -1, (255), thickness=cv2.FILLED)

    cv2.imshow('normal',imagen)
    # cv2.imshow('binarizada',imagen_binaria)
    cv2.imshow('contornos',imagen_contornos)
    cv2.imshow('nueva',imagen_n)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

eliminarletras()