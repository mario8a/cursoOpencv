import cv2
import numpy as np

#cargando imagen
imagen = cv2.imread("figuras3d.jpg")
#estableciendo color gris a la imagen
gris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
#tipo flotante 32
gris = np.float32(gris)

#aplicando metodo Harris
imgHarris = cv2.cornerHarris(gris,2,3,0.04)

#utilizando dos variables altura y anchura
height,width = imgHarris.shape
color = (0,255,0)
#recorre la altura de la imagen
for y in range(0,height):
    #recorre la anchura de la imagen
    for x in range(0,width):
        #si la esquina cumple con el rango se pinta un circulo
        if imgHarris.item(y,x) > 0.01 * imgHarris.max():
            cv2.circle(imagen,(x,y),3,color,cv2.FILLED,cv2.LINE_AA)

#mostrar imagen harris
cv2.imshow("Resultado Harris",imgHarris)
#muestra las esquinas
cv2.imshow("Corner Harris",imagen)
#espera tecla para cerrar ventana
cv2.waitKey(0)
#lo vacia de la memoria RAM
cv2.destroyAllWindows()
