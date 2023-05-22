import cv2
import numpy as np
from pyzbar import pyzbar
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

def extraer_numeros_codigo_barras(ruta_imagen):
    # Cargar la imagen
    img = cv2.imread(ruta_imagen)

    # Convertir la imagen a escala de grises
    img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Mostrar la imagen original
    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Imagen original')

    # Detectar los códigos de barras en la imagen
    codigos_barras = pyzbar.decode(img_gris)

    # Mostrar la imagen en escala de grises
    plt.subplot(2, 2, 2)
    plt.imshow(img_gris, cmap='gray')
    plt.title('Imagen en escala de grises')

    # Arreglo para almacenar los números del código de barras
    numeros_codigo = []

    # Mostrar los códigos de barras y extraer los números en formato ASCII
    for codigo in codigos_barras:
        # Extraer los números del código de barras y guardarlos en un arreglo separado
        numeros = [int(digito) for digito in codigo.data.decode("ascii")]
        numeros_codigo.append(numeros)  # Agregar el arreglo de números al arreglo existente

        # Obtener las coordenadas del código de barras
        x, y, w, h = codigo.rect

        # Dibujar un rectángulo alrededor del código de barras
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)

        # Crear una imagen PIL a partir de la imagen OpenCV
        pil_image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(pil_image)

        # Cargar una fuente para renderizar los caracteres ASCII en color azul
        font = ImageFont.truetype("arial.ttf", 10)

        # Mostrar los números del código de barras en formato ASCII en color azul
        for i, numero in enumerate(numeros):
            # Calcular posición para mostrar cada número
            offset_x = int(x + (w / len(numeros)) * i)
            offset_y = y - 15

            # Transformar el número en formato ASCII a lenguaje natural
            numero_ascii = ord(str(numero))


            # Renderizar el número del código de barras en formato ASCII en la imagen PIL 
            draw.text((offset_x, offset_y), str(numero_ascii), font=font, fill=(0, 0, 255))

        # Convertir la imagen PIL de nuevo a OpenCV
        img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

    # Mostrar la imagen con los códigos de barras y su descripción
    plt.subplot(2, 2, 3)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Códigos de barras con descripción')

    # Ajustar el diseño y mostrar las imágenes
    plt.tight_layout()
    plt.show()
 # Imprimir los arreglos con los números del código de barras
    for i, numeros in enumerate(numeros_codigo):
        print(f"Números del código de barras {i+1}:", numeros)

    # Obtener el código ASCII de manera individual
    codigos_ascii = [[chr(numero) for numero in numeros] for numeros in numeros_codigo]

    # Imprimir los códigos ASCII individuales
    for i, codigos in enumerate(codigos_ascii):
        print(f"Código ASCII individual {i+1}:", codigos)

# Ruta de la imagen con el código de barras
ruta_imagen = "./pictures/codigo1.png"

# Llamar a la función para extraer los números del código de barras
extraer_numeros_codigo_barras(ruta_imagen)