import cv2
import matplotlib.pyplot as plt

# Cargar las imágenes
imagen1 = cv2.imread('./pictures/llanta.jpg', 0)
imagen2 = cv2.imread('./pictures/llanta.jpg', 0)

# Calcular los histogramas de las imágenes
histograma1 = cv2.calcHist([imagen1], [0], None, [256], [0, 256])
histograma2 = cv2.calcHist([imagen2], [0], None, [256], [0, 256])

# Crear una figura con una cuadrícula de subparcelas
fig, axs = plt.subplots(2, 2)

# Mostrar las imágenes en las subparcelas superiores
axs[0, 0].imshow(imagen1, cmap='gray')
axs[0, 0].set_title('Imagen 1')

axs[0, 1].imshow(imagen2, cmap='gray')
axs[0, 1].set_title('Imagen 2')

# Mostrar los histogramas en las subparcelas inferiores
axs[1, 0].plot(histograma1, color='black')
axs[1, 0].set_title('Histograma 1')
axs[1, 0].set_xlabel('Niveles de intensidad')
axs[1, 0].set_ylabel('Frecuencia')

axs[1, 1].plot(histograma2, color='black')
axs[1, 1].set_title('Histograma 2')
axs[1, 1].set_xlabel('Niveles de intensidad')
axs[1, 1].set_ylabel('Frecuencia')

# Ajustar el espaciado entre las subparcelas
plt.tight_layout()

# Mostrar la figura con las subparcelas
plt.show()
