import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen 
imagen= cv2.imread('./pictures/captura4.jpg',cv2.IMREAD_GRAYSCALE)

# binarizamos con otsu
_, imagen_binaria = cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Invertir la imagen binaria
imagen_negativa = cv2.bitwise_not(imagen_binaria)

# Aplicar el etiquetado de componentes
num_componentes, etiquetas, stats, centroides = cv2.connectedComponentsWithStats(imagen_negativa)



# variable auxiliar para eliminar objetos pequeños
aux = 0
porcentaje = 0
# Mostrar los estadísticas de los componentes (área, coordenadas del rectángulo delimitador)
for i in range(1, num_componentes):  # Excluyendo el fondo con etiqueta 0
    #print('Componente', i)
    #print('Área:', stats[i, cv2.CC_STAT_AREA])
    #print('Rectángulo delimitador:', stats[i, cv2.CC_STAT_LEFT], stats[i, cv2.CC_STAT_TOP],stats[i, cv2.CC_STAT_WIDTH], stats[i, cv2.CC_STAT_HEIGHT])
    
    if stats[i, cv2.CC_STAT_AREA]  > aux:
        aux = stats[i, cv2.CC_STAT_AREA]
        porcentaje = aux * 0.3
    
    if stats[i, cv2.CC_STAT_AREA] < porcentaje:

        # Crear una máscara para filtrar objetos pequeños
        mascara_objetos_pequenos = np.zeros_like(imagen_negativa, dtype=np.uint8)

        # Iterar sobre las etiquetas de los componentes
        for i in range(1, num_componentes):
            # Obtener el tamaño del componente actual
            tamano_componente = etiquetas[etiquetas == i].size

            # Si el tamaño del componente es mayor o igual al tamaño mínimo, agregarlo a la máscara
            if tamano_componente >= porcentaje:
                mascara_objetos_pequenos[etiquetas == i] = 255

        # Aplicar la máscara a la imagen original para eliminar los objetos pequeños
        imagen_sin_objetos_pequenos = cv2.bitwise_and(imagen_negativa, imagen_negativa, mask=mascara_objetos_pequenos)


    #print('mayor', aux)
    #print('porcentaje', porcentaje)

# Color del rectángulo delimitador (en formato BGR)
color_verde = (0, 255, 0)
# Color del centroide rojo
color_rojo = (0, 0, 255)


# Dibujar los rectángulos delimitadores + centroid en la imagen 
imagen_con_rectangulos = cv2.cvtColor(imagen_negativa, cv2.COLOR_GRAY2BGR)

for i in range(1, num_componentes):
    #centroid
    x_centroide = int(centroides[i][0])
    y_centroide = int(centroides[i][1])
    cv2.circle(imagen_con_rectangulos, (x_centroide, y_centroide), 2, color_rojo, -1)
    #rectangulos delimitadores
    x, y, w, h = cv2.boundingRect((etiquetas == i).astype(np.uint8))
    cv2.rectangle(imagen_con_rectangulos, (x, y), (x+w, y+h), color_verde, 2)


# Mostrar el número total de componentes
print('Número total de componentes:', num_componentes-1)

# Crear una figura con una cuadrícula de subparcelas
fig, axs = plt.subplots(3, 2)

for i in range(3):
    for j in range(2):
        axs[i, j].axis('off')


axs[0,0].imshow(imagen, cmap='gray')
axs[0,0].set_title('Imagen original')
axs[0,1].imshow(imagen_binaria, cmap='gray')
axs[0,1].set_title('Imagen binaria')
axs[1,0].imshow(imagen_negativa, cmap='gray')
axs[1,0].set_title('Imagen negativa')
axs[1,1].imshow(etiquetas.astype('uint8') * (255 // num_componentes), cmap='gray')
axs[1,1].set_title('Imagen etiquetada')
axs[2,0].imshow(imagen_con_rectangulos, cmap='gray')
axs[2,0].set_title('Bounding + Centroid')
axs[2,1].imshow(imagen_sin_objetos_pequenos, cmap='gray')
axs[2,1].set_title('Eliminacion de figuras')

# Ajustar el espaciado entre las subparcelas
plt.tight_layout()
# Mostrar la figura con las subparcelas
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
