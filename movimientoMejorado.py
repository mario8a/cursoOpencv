#DETECTANDO MOV CON UN PUNTO
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#cap.set(3,320)#Ancho
#cap.set(4,240)#Alto
# leyendo una imagen (previa) que va restar la imagen actual
_,prev = cap.read()
#Convirtiendo a escala de grises
prevG = cv2.cvtColor(prev, cv2.COLOR_RGB2GRAY)
#kernel nos va servir para eliminar el ruido. np.ones crea una matruz
kernel = np.ones((5,5),np.uint8)

font = cv2.FONT_HERSHEY_SIMPLEX

PrevCen = np.array([0,0])
while True:
    _,next = cap.read()
    #transformado a gray
    nextG = cv2.cvtColor(next, cv2.COLOR_RGB2GRAY)
    flow = np.array(abs(np.array(nextG,np.float32)-np.array(prevG,np.float32)),np.uint8)
    #Ahora la diferecia va hacer la diferecia en las img formato gris
    cv2.imshow('flow',flow)
    #Habia una parte negra y la blanca que era el contorno,
    # esos espacios blancos al final tienen un valor
    #deben tener 5 5-5, y no queremos que detecte eso,
    #solo lo que se mueva y solo detectaremos los pixelex
    #que esten en un determinado rango #Diferencia mayor a 20
    rang = cv2.inRange(flow,20,255)
    cv2.imshow('rang',rang)
    #openn eliminar el ruido blanco en zonas negraas
    #closs lo contrario a open elimina el ruido en las areas blancas
    opening = cv2.morphologyEx(rang, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('closing',closing)

    _,contours,_ = cv2.findContours(closing,1,2)

    M = [0,0]#creando un punto#2
    n = 0#valor para que pueda sumar#2
    for cnt in contours:#porque va detectar muchos contornos
    #Con boundingRect extrae los valores del x=punto inicial
    # final y W ancho y H alto 
        x,y,w,h = cv2.boundingRect(cnt)
        # si el punto que se mueve es de 15px lo va detectar
        if w>15 and h>15 and w<200 and h<200:
            #Detectar los centros y sumarlos a un valor y al final obtener el promedio
            #de todos los contornos que se han detectado
            M[0] += x + float(w)/2.
            M[1] += y + float(h)/2.
            n += 1
#Dibujando un circulo
    if M[0]!=0 and M[0]!=0:
        #conviriento a un array
        M = np.array(M)
        #El mov del circulo no sea tan brusco. valor 0 es en medio del mov
        NewCen = PrevCen + 0.5*(M-PrevCen)
        #buscando el centro
        cntX = int(NewCen[0]/n)
        cntY = int(NewCen[1]/n)
        #El 5 es el tamano 5 para que sea un circulo
        cv2.circle(next,(cntX,cntY),5,(130,50,200),-1)
        #el valor 10 es para que no salga en el centro del circulo
        cv2.putText(next,str(cntX)+","+str(cntY),(cntX+10,cntY+10),font,1,(130,50,200),3)
        PrevCen = NewCen

    prevG = nextG

    cv2.imshow('next',next)
    if cv2.waitKey(1) & 0xFF == ord ('q'):
        break

    #k = cv2.waitKey(1) & 0xFF
    #if k == 27: break

cap.release()
cv2.destroyAllWindows()

#El pixel 0.0 esta en la esqina sup izq y los ultimos estan en esq abajo a la derecha
#Flow detecta solo los contornos
#rang resalto los contrornos
#closing intento cerrar los contornos
