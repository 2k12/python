import cv2
import matplotlib.pyplot as plt


def main():
    # Cargar la imagen en escala de grises
    imagen = cv2.imread('./pictures/llanta.jpg', cv2.IMREAD_GRAYSCALE)

    # Aplicar la ecualización del histograma
    imagen_ecualizada = cv2.equalizeHist(imagen)

    # Calcular el histograma de la imagen
    histograma = cv2.calcHist([imagen_ecualizada], [0], None, [256], [0, 256])

    # Mostrar el histograma
    plt.plot(histograma, color='black')
    plt.xlabel('Niveles de intensidad')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de la imagen')



    # Mostrar la imagen original y la imagen ecualizada
    cv2.imshow('Imagen original', imagen)
    cv2.imshow('Imagen ecualizada', imagen_ecualizada)
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

