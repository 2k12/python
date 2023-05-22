
import cv2
import matplotlib.pyplot as plt
import numpy as np


def carga_de_imagen():
    op = int(input('ingrese la imagen que desea cargar { 1,2,3 }: '))
    lista = []
    if op == 1:
        imagen = cv2.imread('./pictures/puntos_lineas.jpg',cv2.IMREAD_GRAYSCALE)
        radio = 9
        lista.append(imagen)
        lista.append(radio)
    elif op == 2:
        imagen = cv2.imread('./pictures/puntos_lineas_2.png',cv2.IMREAD_GRAYSCALE)
        radio = 4
        lista.append(imagen)
        lista.append(radio)
        
    elif op == 3:
        imagen = cv2.imread('./pictures/puntos_lineas_3.png',cv2.IMREAD_GRAYSCALE)
        radio = 6
        lista.append(imagen)
        lista.append(radio)
    else:
        op=0
    
    return lista



def ejercicio():
    #cargar imagen
    lista= carga_de_imagen()
    # elementos
    imagen = lista[0]
    radio = lista[1]
    
    
    # binarizamos con otsu
    umbral1, imagen_binaria = cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    #elemento estructural
    se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (radio,radio))

    #elemento estructural
    se2 = cv2.getStructuringElement(cv2.MORPH_RECT,(15,1))
    se3 = cv2.getStructuringElement(cv2.MORPH_RECT,(1,15))



    # Aplicar la apertura
    imagen_apertura = cv2.morphologyEx(imagen_binaria, cv2.MORPH_OPEN, se)
    imagen_apertura2 = cv2.morphologyEx(imagen_binaria, cv2.MORPH_RECT, se2)
    imagen_apertura3 = cv2.morphologyEx(imagen_binaria, cv2.MORPH_RECT, se3)


    #deteccion de bordes
    # * CANNY
    bordesc = cv2.Canny(imagen_apertura, 1, 100)

    # * LAPLACIANO
    bordesc2 = cv2.Laplacian(imagen_apertura, cv2.CV_64F)
    # Convertir los valores a enteros sin signo
    bordesc2 = cv2.convertScaleAbs(bordesc2)

    # # * SOBEL
    # Aplicar el operador Sobel en el eje X
    sobel_x = cv2.Sobel(imagen_apertura, cv2.CV_64F, 1, 0, ksize=3)

    # Aplicar el operador Sobel en el eje Y
    sobel_y = cv2.Sobel(imagen_apertura, cv2.CV_64F, 0, 1, ksize=3)

    # Calcular el gradiente absoluto
    gradiente_absoluto = np.sqrt(sobel_x**2 + sobel_y**2)

    # Binarizar la imagen resultante
    umbral = 100  # Puedes ajustar este valor según tus necesidades
    _, imagen_sobel = cv2.threshold(gradiente_absoluto, umbral, 255, cv2.THRESH_BINARY)
    # Convertir la imagen binaria a tipo de dato de 8 bits sin signo
    imagen_sobel = imagen_sobel.astype(np.uint8)

    # Aplicar el etiquetado de componentes


    num_componentes1, etiquetas2, stats2, centroides2 = cv2.connectedComponentsWithStats(imagen_apertura)
    num_componentes1=num_componentes1-1

    num_componentes2, etiquetas2, stats2, centroides2 = cv2.connectedComponentsWithStats(imagen_apertura2)
    num_componentes2=num_componentes2-1

    num_componentes3, etiquetas3, stats3, centroides3 = cv2.connectedComponentsWithStats(imagen_apertura3)
    num_componentes3=num_componentes3-1

    num_componentest = num_componentes2+num_componentes3

    # ! ----------------USANDO DETECCION DE BORDES---------------------

    # ! componentes usando canny
    num_componentes, etiquetas, stats, centroides = cv2.connectedComponentsWithStats(bordesc)
    num_componentes=num_componentes-1
    # ! componentes usando sobel
    num_componentes4, comp4 = cv2.connectedComponents(imagen_sobel)
    num_componentes4=num_componentes4-1
    # ! componenter usando laplacian
    num_componentes5, etiquetas5, stats5, centroides = cv2.connectedComponentsWithStats(bordesc2)
    num_componentes5=num_componentes5-1


    # Mostrar el número total de componentes (incluyendo el fondo)
    if radio == 6:
        print('Número total de circulos es:', num_componentes1) 
        print('Número total de circulos usando canny:', num_componentes)
        print('Número total de circulos usando sobel:', num_componentes4)
        print('Número total de circulos usando laplacian:', num_componentes5)
    else:
        print('Número total de circulos es:', num_componentes1) 
        print('Número total de circulos usando canny:', num_componentes)
        print('Número total de circulos usando sobel:', num_componentes4)
        print('Número total de circulos usando laplacian:', num_componentes5)
        print('Número total de lineas horizontales:', num_componentes2) 
        print('Número total de lineas verticales:', num_componentes3)
        print('Número total de lineas es:', (num_componentest))

    if radio == 6:
        cv2.imshow('binarizada', imagen_binaria)
        cv2.imshow('normal', imagen)
        cv2.imshow('apertura', imagen_apertura)
        cv2.imshow('canny', bordesc)  
        cv2.imshow('laplaciano', bordesc2) 
        cv2.imshow('sobel', imagen_sobel)  
    else:        
    #mostrar imagenes
        cv2.imshow('binarizada', imagen_binaria)
        cv2.imshow('normal', imagen)
        cv2.imshow('apertura', imagen_apertura)
        cv2.imshow('lineas h', imagen_apertura2)   
        cv2.imshow('lineas v', imagen_apertura3)  
        cv2.imshow('canny', bordesc)  
        cv2.imshow('laplaciano', bordesc2) 
        cv2.imshow('sobel', imagen_sobel)  


    cv2.waitKey(0)
    cv2.destroyAllWindows()



