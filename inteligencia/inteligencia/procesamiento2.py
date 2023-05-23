import cv2
import matplotlib.pyplot as plt


def main():
    # Cargar la imagen en escala de grises
    imagen = cv2.imread('./pictures/llanta.jpg', cv2.IMREAD_GRAYSCALE)

    # Aplicar la ecualización del histograma
    imagen_ecualizada = cv2.equalizeHist(imagen)

    # Calcular el histograma de la imagen
    histograma = cv2.calcHist([imagen_ecualizada], [0], None, [256], [0, 256])

    fig,axs = plt.subplots(1, 3)

    for i in range(2):
        axs[i].axis('off') 

    axs[0].imshow(imagen, cmap='gray')
    axs[0].set_title('Imagen Original')
    axs[1].imshow(imagen_ecualizada, cmap='gray')
    axs[1].set_title('Imagen Ecualizada')
    axs[2].plot(histograma, color='green')
    axs[2].set_title('Histograma de la imagen')
    axs[2].set_xlabel('Niveles de intensidad')
    axs[2].set_ylabel('Frecuencia')

    plt.tight_layout()
    plt.show()

