#Python
from math import *
import numpy as np

#Librerías propias
from utils.calculo_juntas.obtener_trayectorias import obtener_trayectoria


#Programa principal
def run():
    #Creación de las listas con las trayectorias
    q0v=[]
    q1v=[]
    q2v=[]

    #Configuración fisica de las patas traseras
    Z0 = 33.84;
    L1 = 100;
    L2 = 70;
    L3 = 60;

    POSICION_SERVO_HOMBRO = 0

    #Asignación de los puntos
    xC, yC = obtener_trayectoria()

    tamano = xC.size

    for i in range(tamano):
        x=xC[i]
        y=yC[i]
        z=0

        p0 = [x,y,z] 
        
        alpha = acos(z/sqrt(z**2+y**2))
        phi = atan2(y,z)
        q0=POSICION_SERVO_HOMBRO
        
        if alpha>abs(phi):
            q0=phi+alpha
        else:
            q0=phi+alpha
        
        #Rotación del plano
        R = np.array([[1, 0, 0],
            [0, cos(-q0), -sin(-q0)],
            [0, sin(-q0), cos(-q0)]])
        
        d = np.transpose(np.array([0, Z0*sin(q0), Z0*cos(q0)]))
        
        p1 = np.linalg.inv(R)*(p0-d)
        
        #Calculo de q1,q2 y q3
        xc = p1[0][0]
        yc = p1[1][1]
        
        a = (L3*L2)/(L1+L3)
        b = (L3*sqrt(xc**2+yc**2))/(L1+L3)

        beta = acos((b**2+L3**2-a**2)/(2*b*L3))
        theta = atan2(yc,xc)
        
        if beta>abs(theta):
            q1=beta+theta
        else:
            q1=theta+beta
        
        #Resumen variables
        q0=q0.real
        q1=q1.real
        q2 = acos((a**2+L3**2-b**2)/(2*a*L3)).real
        q3 = q2
        
        q0v.append(q0)
        q1v.append(q1)
        q2v.append(q2)

        print(q1v)

    q0v.extend(q0v[:-1])
    q1v.extend(q1v[:-1])
    q2v.extend(q2v[:-1])

    print(q0v)


#Entry point
if __name__ == '__main__':
    run()