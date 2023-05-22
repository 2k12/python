import cv2
import numpy as np
import matplotlib.pyplot as plt

def boundin_centr_llaves():
    img = cv2.imread('pictures/llaves.png',0)
    img = cv2.bitwise_not(img)
    _,imagen_binaria = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    # Color del rectángulo delimitador (en formato BGR)
    color_verde = (0, 255, 0)
    # Color del centroide rojo
    color_rojo = (0, 0, 255)

    num_componentes,  etiquetas, stats, centroides = cv2.connectedComponentsWithStats(imagen_binaria)
    

    # Dibujar los rectángulos delimitadores + centroid en la imagen 
    imagen_con_rectangulos = cv2.cvtColor(imagen_binaria, cv2.COLOR_GRAY2BGR)

    for i in range(1,num_componentes):
        #centroid
        x_centroide = int(centroides[i][0])
        y_centroide = int(centroides[i][1])
        cv2.circle(imagen_con_rectangulos, (x_centroide, y_centroide), 2, color_rojo, -1)
        #rectangulos delimitadores
        x, y, w, h = cv2.boundingRect((etiquetas == i).astype(np.uint8))
        cv2.rectangle(imagen_con_rectangulos, (x, y), (x+w, y+h), color_verde, 2)

    num_componentes = num_componentes-1
    print('llaves: ',num_componentes)
    cv2.imshow('binarizada', imagen_binaria)
    cv2.imshow('bounding + centroid', imagen_con_rectangulos)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




