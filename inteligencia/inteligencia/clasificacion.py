import cv2
import numpy as np 
import matplotlib.pyplot as plt

def main():
    imagen = cv2.imread('./pictures/llaves.png',0)
    _,imagen_binarizada = cv2.threshold(imagen,0,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    imagen_negativa = cv2.bitwise_not(imagen_binarizada)



    #impresion de las imagenes
    fig,axs = plt.subplots(2,2)

    for i in range(2):
        for j in range(2):
            axs[i, j].axis('off')

    axs[0,0].imshow(imagen, cmap='gray')
    axs[0,0].set_title('Imagen Normal')
    axs[0,1].imshow(imagen_binarizada, cmap='gray')
    axs[0,1].set_title('Imagen Binarizada')
    axs[1,0].imshow(imagen_negativa, cmap='gray')
    axs[1,0].set_title('Imagen Negativa')
    # axs[1,1].imshow('imagen', cmap='gray')
    # axs[1,1].set_title('Imagen Normal')
    


    plt.tight_layout()
    plt.show()

main()