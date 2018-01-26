#DETECTANDO 3 COLORES
import cv2
import numpy as np


cap=cv2.VideoCapture(0)

while(True):
	_, img = cap.read()


	#convertimos el frame a HSV, esto e sun modelo de colores parecido
	#al RGB. por sus siglas Hue, Saturation, Velue(matriz, Saturacion, valor)

	hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

	#definir el rango del color rojo
	rojo_min=np.array([136,87,111],np.uint8)
	rojo_max=np.array([180,255,255],np.uint8)

	
	azul_min=np.array([99,115,150],np.uint8)
	azul_max=np.array([110,255,255],np.uint8)

	
	yellow_min=np.array([22,60,200],np.uint8)
	yellow_max=np.array([60,255,255],np.uint8)

	#definiendo rango de imagen
	red=cv2.inRange(hsv, rojo_min, rojo_max)
	blue=cv2.inRange(hsv,azul_min,azul_max)
	yellow=cv2.inRange(hsv,yellow_min,yellow_max)

	#Transformacion morfologica y  Dilatacion del color

	kernel = np.ones((5 ,5),np.uint8)
	## Masscara de bit a bit AND e imagen original
    	rojo=cv2.dilate(red, kernel)
	res=cv2.bitwise_and(img, img, mask = rojo)

	azul=cv2.dilate(blue,kernel)
	res1=cv2.bitwise_and(img, img, mask = azul)

	yellow=cv2.dilate(yellow,kernel)
	res2=cv2.bitwise_and(img, img, mask = yellow)

	#Cuando se itera sobre una secuencia, se puede obtener el
	#indice de posicion junto a su valor correspondiente usando la funcion enumerate
	#hierarchy da un Vector de salida opcional que contiene informacion sobre la topologia de la imagen
	#RETR TREE calcula la jerarquia completa de los contornos
	#Chain_Aproxx que elimina todos los puntos redundantes
#ROJO
	(_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>300):

			x,y,w,h = cv2.boundingRect(contour)
			img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
			cv2.putText(img,"Color Rojo",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))

	#AZUL
	(_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>300):
			x,y,w,h = cv2.boundingRect(contour)
			img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
			cv2.putText(img,"Color Azul",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))

	#AMARILLO
	(_,contours,hierarchy)=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>300):
			x,y,w,h = cv2.boundingRect(contour)
			img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
			cv2.putText(img,"Color Amarillo",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0))
			#El 1.0 es para que el texto no este en el centro


    	
    	cv2.imshow("Deteccion de colores RGB",img)
    	
    	if cv2.waitKey(10) & 0xFF == ord('q'):
    		cap.release()
    		cv2.destroyAllWindows()
    		break
