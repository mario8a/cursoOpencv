import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#cap = cv2.CaptureFromCAM(-1)

cap.set(3,320)#px,Alto
cap.set(4,240)#px,Ancho


while True:
    ret, frame = cap.read()

    cv2.imshow('video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
