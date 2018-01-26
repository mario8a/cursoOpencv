import numpy as np
import cv2

img = "sudoku.png"

gris = cv2.imread(img, cv2.IMREAD_GRAYSCALE)

# umbral fijo
_, segmentar = cv2.threshold(gris, 80, 255, cv2.THRESH_BINARY)

cv2.imshow('umbral fijo', segmentar)

# umbral adaptable
gris = cv2.medianBlur(gris, 5)
segmentar2 = cv2.adaptiveThreshold(gris, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('umbral adaptable', segmentar2)

cv2.waitKey(0)
cv2.destroyAllWindows()
