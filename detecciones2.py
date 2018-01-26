import cv2
import numpy as np
#carga imagen
img = cv2.imread("figuras3d.jpg")
#la convierte en gris
gris = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#utiliza metodo para detectar las esquinas
esquinas = cv2.goodFeaturesToTrack(gris,40,0.01,10)
#trabaja con enteros
esquinas = np.int0(esquinas)
#recorre la imagen, para obtener la coordenada de donde estan las esquinas
for i in esquinas:
    #metodo que contiene coordenadas
    x,y = i.ravel()
    #pinta circulo en donde esta la esquina
    cv2.circle(img,(x,y),3,(0,255,0),-1)
#muestra en ventana
cv2.imshow("Esquinas",img)
#espera tecla
cv2.waitKey(0)
#libera de la memoria
cv2.destroyAllWindows()
