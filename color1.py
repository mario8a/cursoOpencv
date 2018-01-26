#detectando color rojo
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsv =  cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    rojo_min = np.array([136,87,111])
    rojo_max = np.array([180,255,255])

    mascara = cv2.inRange(hsv, rojo_min, rojo_max)

    bits = cv2.bitwise_and(frame, frame, mask = mascara)

    cv2.imshow('frame',frame)
    cv2.imshow('Mascara',mascara)
    cv2.imshow('bits',bits)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
