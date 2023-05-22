import cv2
import numpy as np
import matplotlib.pyplot as plt

def obtenerlineasdelcbd():
    imagen = cv2.imread('./pictures/lata1.png')
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # imagen = cv2.bitwise_not(imagen)



    # Color del rectángulo delimitador (en formato BGR)
    color_verde = (0, 255, 0)
    # Color del centroide rojo
    color_rojo = (0, 0, 255)


    # Dibujar los rectángulos delimitadores + centroid en la imagen 
    imagen_con_rectangulos = cv2.cvtColor(imagen, cv2.COLOR_GRAY2BGR)
        # Aplicar el etiquetado de componentes
    num_componentes, etiquetas, stats, centroides = cv2.connectedComponentsWithStats(threshold)
    num_componentes = num_componentes - 1 
    # Mostrar el número total de componentes (incluyendo el fondo)
    print('Número total de componentes:', num_componentes)
    for i in range(1, num_componentes):
        if stats[i, cv2.CC_STAT_AREA]  > 900 and stats[i, cv2.CC_STAT_AREA] <= 2000:
            #centroid
            x_centroide = int(centroides[i][0])
            y_centroide = int(centroides[i][1])

            cv2.circle(imagen_con_rectangulos, (x_centroide, y_centroide), 2, color_rojo, -1)
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
    # * escalamiento
    # Definir el tamaño de escalado deseado
    new_width = 100
    new_height = 200

    # Escalar la región recortada a las nuevas dimensiones
    scaled_roi = cv2.resize(content, (new_width, new_height))
    #  * ------------------------------------------
    # * aumento de brilloooooooooooooooo
    scaled_float = scaled_roi.astype(np.float32)
    # Definir el factor de aclarado (ejemplo: 1.2 para aumentar el brillo)
    brightness_factor = 1.2

    # Aplicar el factor de aclarado a la imagen
    brightened_image = scaled_float * brightness_factor

    # Asegurarse de que los valores de píxeles no excedan el rango máximo de 255
    brightened_image = np.clip(brightened_image, 0, 255)

    # Convertir la imagen de nuevo a tipo uint8
    brightened_image = brightened_image.astype(np.uint8)
    # * --------------------------------------------------

    roig = cv2.cvtColor(brightened_image, cv2.COLOR_BGR2GRAY)
    
    # Aplicar umbralización para convertir la imagen en binaria
    _, binary = cv2.threshold(roig, 127, 255, cv2.THRESH_BINARY)
    # Obtener el tamaño del kernel para la operación de dilatación
    kernel_size = int(content.shape[1] / 40)

    # Definir el kernel estructurante para la operación de dilatación
    kernel = np.ones((1, kernel_size), dtype=np.uint8)

    # Realizar una operación de dilatación para unir las líneas horizontales
    dilated = cv2.dilate(binary, kernel, iterations=1)

    # Encontrar los contornos de las líneas dilatadas
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Extraer las líneas horizontales
    horizontal_lines = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = w / float(h)
        if aspect_ratio > 5:  # Filtrar contornos con un aspecto alargado
            horizontal_lines.append(contour)

    # Crear una imagen en blanco del mismo tamaño que el contenido
    result = np.zeros_like(scaled_roi)

    # Dibujar las líneas horizontales en la imagen resultante
    cv2.drawContours(result, horizontal_lines, -1, (0, 0, 255), thickness=1)

    # Mostrar la imagen resultante con las líneas horizontales resaltadas
    cv2.imshow('Brightened Image', brightened_image)
    cv2.imshow('Horizontal Lines', result)
    cv2.imshow('content',roig)
    cv2.imshow('inversa',imagen)
    cv2.imshow('Imagen Bounding + Centroid', imagen_con_rectangulos)
    # cv2.imshow('Imagen etiquetada', etiquetas.astype('uint8') * (255 // num_componentes))
    # cv2.imshow('threshold',threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

obtenerlineasdelcbd()

