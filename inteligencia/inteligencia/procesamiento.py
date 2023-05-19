import cv2
import matplotlib.pyplot as plt

# Cargar la imagen
imagen = cv2.imread('./pictures/llanta.jpg')

# Convertir la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)


# Calcular el histograma de la imagen
histograma = cv2.calcHist([imagen_gris], [0], None, [256], [0, 256])

# Crear una figura con una cuadrícula de subparcelas
fig, axs = plt.subplots(1, 2)



# Ajustar los valores de intensidad en escala de grises
# ? imagen_gris_ajustada = # Aplicar técnicas de inteligencia artificial para ajustar los valores de intensidad

# Convertir la imagen a RGB
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

# Ajustar los valores de intensidad en RGB
# ? imagen_rgb_ajustada = # Aplicar técnicas de inteligencia artificial para ajustar los valores de intensidad

# Mostrar las imágenes originales y ajustadas

# ? cv2.imshow('Imagen en escala de grises ajustada', imagen_gris_ajustada)
# * cv2.imshow('Imagen RGB', imagen_rgb)
# ? cv2.imshow('Imagen RGB ajustada', imagen_rgb_ajustada)

# Mostrar las imágenes en las subparcelas superiores
axs[0].imshow(imagen_gris, cmap='gray')
axs[0].set_title('Escala de Grises')

# Mostrar los histogramas en las subparcelas inferiores
axs[1].plot(histograma, color='black')
axs[1].set_title('Histograma')
axs[1].set_xlabel('Niveles de intensidad')
axs[1].set_ylabel('Frecuencia')


# Ajustar el espaciado entre las subparcelas
plt.tight_layout()

# Mostrar la figura con las subparcelas
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
