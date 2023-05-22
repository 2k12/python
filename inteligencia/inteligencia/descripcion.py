import cv2
import numpy as np
import matplotlib.pyplot as plt

def orientacion_img():
    # captura
    g = cv2.imread('./pictures/orientacion.png')

    # preprocesamiento
    if g.shape[2] == 3:  # es RGB?
        g = cv2.cvtColor(g, cv2.COLOR_BGR2GRAY)
    plt.subplot(2, 2, 1)
    plt.imshow(g, cmap='gray')

    # segmentacion
    umbral, bw = cv2.threshold(g, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    plt.subplot(2, 2, 2)
    plt.imshow(bw, cmap='gray')

    kernel = np.ones((5, 5), np.uint8)
    bw2 = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)  # rellenar el objeto
    plt.subplot(2, 2, 3)
    plt.imshow(bw2, cmap='gray')

    # descripcion
    contours, _ = cv2.findContours(bw2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    rect = cv2.minAreaRect(contours[0])
    ang = rect[2]  # ángulo en sentido contrario a las manecillas del reloj
    if ang > -45:
        ang -= 90
    Ir = cv2.warpAffine(bw, cv2.getRotationMatrix2D(rect[0], ang, 1.0), (bw.shape[1], bw.shape[0]))
    plt.subplot(2, 2, 4)
    plt.imshow(Ir, cmap='gray')

    plt.title('Rotada: {}'.format(ang))
    plt.tight_layout()
    plt.show()
