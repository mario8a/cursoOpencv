#detectando movimiento

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

a, prev = cap.read()

while True:
    #Restar los valores de las dos imagens
    a,imgA = cap.read()
    mov = np.array(abs(np.array(imgA,np.float32)-np.array(prev,np.float32)),np.uint8)

    cv2.imshow('Movimiento', mov)

    prev = imgA

    #cv2.imshow('videoNormal',imgA)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
