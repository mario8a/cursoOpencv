import cv2
import numpy as np

"""Events"""
"""
EVENT_LBUTTONDOWN
EVENT_MBUTTONDOWN
EVENT_RBUTTONDOWN
EVENT_LBUTTONUP
EVENT_MBUTTONUP
EVENT_RBUTTONUP
EVENT_LBUTTONDBLCLK
EVENT_MBUTTONDBLCLK
EVENT_RBUTTONDBLCLK
"""

fondo = np.zeros((700,1000,4),np.uint8)

pintar = False
ix,iy = 0,0

def dibujar(evento,x,y,flags,params):
	
	global pintar,ix,iy

	if(evento == cv2.EVENT_LBUTTONDBLCLK):
		cv2.circle(fondo,(x,y),50,(255,0,255),10)
	elif(evento == cv2.EVENT_RBUTTONDBLCLK):
		ix,iy = x,y
		cv2.rectangle(fondo,(ix-40,iy+40),(x,y),(0,255,255),5)
	elif(evento == cv2.EVENT_MOUSEMOVE and pintar):
		cv2.rectangle(fondo,(x,y),(x,y),(255,0,255),5)

cv2.namedWindow("Paint")
cv2.setMouseCallback("Paint",dibujar)

while(True):
	cv2.imshow("Paint",fondo)
	k = cv2.waitKey(1) & 0xFF
	if(k == ord("p")):
		    pintar = not pintar
	elif(k == 27):
		    break
	elif(k == ord("s")):
		    cv2.imwrite("captura.jpg",fondo)


cv2.destroyAllWindows()