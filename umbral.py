import numpy as np
import cv2

#THRESH_BINARY
#THRESH_BINARY_INV
#THRESH_TRUNC
#THRESH_TOZERO
#THRESH_TOZERO_INV

#establece la imagen en gris
gray = cv2.imread('herramientas.jpg', cv2.IMREAD_GRAYSCALE)
#se aplica la segementacion
t, segmentar = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)
#muestra la imagen en gris
cv2.imshow('umbral', gray)
#muestra en ventana la segmentacion
cv2.imshow('result', segmentar)
#esspera tecla para cerrar la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()
