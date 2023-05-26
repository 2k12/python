import cv2
import numpy as np 
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops

def main():
    # cargamos la imagen
    imagen = cv2.imread('./pictures/llaves.png',0)
    # imagen binarizada
    _,imagen_binarizada = cv2.threshold(imagen,0,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # imagen negativa
    imagen_negativa = cv2.bitwise_not(imagen_binarizada)
    #elemento estructurado
    num_componentes, etiquetas, stats, centroides = cv2.connectedComponentsWithStats(imagen_negativa)
    #color verde
    color_verde = (0, 255, 0)
    # Dibujar los rectángulos delimitadores + centroid en la imagen 
    imagen_con_rectangulos = cv2.cvtColor(imagen_negativa, cv2.COLOR_GRAY2BGR)
    for i in range(1, num_componentes):
        #rectangulos delimitadores
        x, y, w, h = cv2.boundingRect((etiquetas == i).astype(np.uint8))
        cv2.rectangle(imagen_con_rectangulos, (x, y), (x+w, y+h), color_verde, 2)
    # impresion numero de componentes encontrados en la imagen
    print('componenetes: ', num_componentes-1)
    # ! ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    # CANNY
    # bordes = cv2.Canny(imagen_negativa,100,255)
    # LAPLACIANO
    bordes = cv2.Laplacian(imagen_negativa, cv2.CV_64F)
    # Convertir los valores a enteros sin signo
    bordes = cv2.convertScaleAbs(bordes)
    # * --------------------------------------
    # Eliminar cierto ruido, puntos aislados
    kernel = np.ones((3,3), np.uint8)
    dil = cv2.morphologyEx(imagen_negativa, cv2.MORPH_DILATE, kernel)
    J = cv2.morphologyEx(dil, cv2.MORPH_ERODE, kernel)
    # Segmentación
    L, num = label(J, return_num=True)
    # Descripción
    props = regionprops(L)
    # Clasificación
    boca = 0
    corona = 0
    # ! ------
    for region in props:
        # euler = region.euler_number
        area = region.area
        # print(area)
        # if euler == 1:
        #     boca += 1
        # elif euler == -1:
        #     corona += 1
        if area < 700:
            boca += 1
        elif area > 700:
            corona += 1

    L1 = L.copy()
    L2 = L.copy()
    for region in props:
        area = region.area
        if area > 700:
            L1[L1 == region.label] = 0  # elimina etiquetas de las de corona
        elif area < 700:
            L2[L2 == region.label] = 0  # elimina etiquetas de las de boca

    bw1 = (L1 != 0).astype(np.uint8)  # boca (binaria)
    bw2 = (L2 != 0).astype(np.uint8)  # corona (binaria)

    # ! ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    #impresion de las imagenes
    fig,axs = plt.subplots(4,2)

    for i in range(4):
        for j in range(2):
            axs[i, j].axis('off')

    axs[0,0].imshow(imagen, cmap='gray')
    axs[0,0].set_title('Imagen Normal')
    axs[0,1].imshow(imagen_binarizada, cmap='gray')
    axs[0,1].set_title('Imagen Binarizada')
    axs[1,0].imshow(imagen_negativa, cmap='gray')
    axs[1,0].set_title('Imagen Negativa')
    # axs[1,1].imshow(J, cmap='gray')
    # axs[1,1].set_title('Imagen apertura')
    axs[1,1].imshow(imagen_con_rectangulos, cmap='gray')
    axs[1,1].set_title('Imagen con rectangulos')    
    axs[2,0].imshow(bordes, cmap='gray')
    axs[2,0].set_title('Bordes Canny')
    axs[2,1].imshow(J, cmap='gray')
    axs[2,1].set_title('Sin Ruido')
    axs[3,0].imshow(bw2, cmap='gray')
    axs[3,0].set_title('Corona: ' + str(corona))
    axs[3,1].imshow(bw1, cmap='gray')
    axs[3,1].set_title('Boca: ' + str(boca))


    
    plt.tight_layout()
    plt.show()
