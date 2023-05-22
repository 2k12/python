import cv2

def main():
    # Cargar la imagen en escala de grises
    imagen = cv2.imread('./pictures/captura4.jpg', cv2.IMREAD_GRAYSCALE)
    
    # Aplicar umbralización de Otsu
    _, imagen_binaria = cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Mostrar la imagen binarizada
    cv2.imshow('Imagen binarizada', imagen_binaria)
    cv2.waitKey(0)
    cv2.destroyAllWindows()