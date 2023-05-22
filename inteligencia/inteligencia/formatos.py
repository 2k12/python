import cv2


def cargarimagen():
    # Cargar la imagen en color
    imagen_color = cv2.imread('./pictures/captura4.jpg')
    # Mostrar la imagen 
    cv2.imshow('Imagen normal', imagen_color)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()


