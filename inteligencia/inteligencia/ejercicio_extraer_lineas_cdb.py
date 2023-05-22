import cv2
import numpy as np
import matplotlib.pyplot as plt
from pyzbar import pyzbar

def obtenerlineasdelcbd():
    imagen = cv2.imread('./pictures/lata1.png')
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # imagen = cv2.bitwise_not(imagen)



    # Color del rectángulo delimitador (en formato BGR)
    color_verde = (0, 255, 0)


    # Dibujar los rectángulos delimitadores + centroid en la imagen 
    imagen_con_rectangulos = cv2.cvtColor(threshold, cv2.COLOR_GRAY2BGR)
    # Aplicar el etiquetado de componentes
    num_componentes, etiquetas, stats, centroides = cv2.connectedComponentsWithStats(threshold)
    num_componentes = num_componentes - 1 
    # Mostrar el número total de componentes (incluyendo el fondo)
    # print('Número total de componentes:', num_componentes)
    for i in range(1, num_componentes):
        if stats[i, cv2.CC_STAT_AREA]  > 900 and stats[i, cv2.CC_STAT_AREA] <= 2000:      
            #rectangulos delimitadores
            x, y, w, h = cv2.boundingRect((etiquetas == i).astype(np.uint8))
            cv2.rectangle(imagen_con_rectangulos, (x, y), (x+w, y+h), color_verde, 2)
            
    # ! ----------------------------------------
    # # Definir los valores de expansión (puedes ajustarlos según tus necesidades)
    # expansion_x = 50
    # expansion_y = 50

    # # Calcular las nuevas coordenadas del rectángulo delimitador expandido
    # new_x = max(0, x - expansion_x)
    # new_y = max(0, y - expansion_y)
    # new_w = min(imagen_con_rectangulos.shape[1], w + 2 * expansion_x)
    # new_h = min(imagen_con_rectangulos.shape[0], h + 2 * expansion_y)

    # # Recortar la región de interés (ROI) utilizando las nuevas coordenadas
    # content = imagen_con_rectangulos[new_y:new_y+new_h, new_x:new_x+new_w]
    # ! ---------------------------------------------------
    content = imagen_con_rectangulos[y:y+h, x:x+w]

    # Mostrar el objeto extraído en una nueva imagen con el bounding box
    object_with_bbox_image = content.copy()
    cv2.rectangle(object_with_bbox_image, (x, y), (x+w, y+h), (0, 255, 0), 2)    

    # Convertir la imagen del objeto a escala de grises
    gray_object_image = cv2.cvtColor(content, cv2.COLOR_BGR2GRAY)

    # Utilizar pyzbar para encontrar y decodificar los códigos de barras en la imagen
    barcodes = pyzbar.decode(gray_object_image)

    # Extraer las líneas del código de barras y mostrarlas en una nueva imagen
    barcode_lines_image = gray_object_image.copy()
    for barcode in barcodes:
        # Obtener las coordenadas del código de barras
        x, y, w, h = barcode.rect

        # Dibujar las líneas del código de barras
        cv2.rectangle(barcode_lines_image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    fig, axs = plt.subplots(2, 2)

    for i in range(2):
        for j in range(2):
            axs[i, j].axis('off')

    axs[0,0].imshow(imagen, cmap='gray')
    axs[0,0].set_title('Imagen Original')
    axs[0,1].imshow(imagen_con_rectangulos, cmap='gray')
    axs[0,1].set_title('Imagen Con Rectangulos')
    axs[1,0].imshow(object_with_bbox_image, cmap='gray')
    axs[1,0].set_title('Objeto con bounding box')
    axs[1,1].imshow(barcode_lines_image, cmap='gray')
    axs[1,1].set_title('Lines del codigo de barras')

    plt.tight_layout()
    plt.show()


    # Mostrar la imagen con las líneas del código de barras
    # cv2.imshow("imagen gris", imagen)
    # cv2.imshow("imagen con rectangulos ", imagen_con_rectangulos)
    # cv2.imshow("Objeto con bounding box", object_with_bbox_image)
    # cv2.imshow("Líneas del código de barras", barcode_lines_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


