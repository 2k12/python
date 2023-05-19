import cv2
import numpy as np

# !! ELEMENTO ESTRUCTURANTE CIRCULO 

# Tamaño del elemento estructurante (radio del círculo)
radio = 3

# Generar un elemento estructurante en forma de círculo
elemento_estructurante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*radio+1, 2*radio+1))

print(elemento_estructurante)
