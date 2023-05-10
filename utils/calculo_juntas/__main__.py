#Python
from math import *
import numpy as np
import json


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

    #Posición inicial de las variables de junta (Radianes)    
    Q0_INICIAL = 0
    Q1_INICIAL = pi/2
    Q2_INICIAL = 0

    #Posiciones MAX y MIN
    Q0_MIN = 0
    Q0_MAX = pi

    Q1_MIN = 0
    Q1_MAX = pi
    
    Q2_MIN = 0
    Q2_MAX = pi

    #Asignación de los puntos
    while 1:
        xC, yC = obtener_trayectoria()
        seleccion = bool(input("Estas de acuerdo con la trayectoria?\n0 -> No\n1 -> Sí: "))
        if seleccion:
            break

    tamano = xC.size

    for i in range(tamano):

        try:
            #Puntos a evaluar 
            x=xC[i]
            y=yC[i]
            z=0

            #Punto en el marco original
            p0 = [x,y,z] 
            
            #Calculo de las variables de juntas
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
                q1 = beta+theta
            else:
                q1 = theta+beta
            
            #Resumen variables
            q0 = q0.real + Q0_INICIAL
            q1 = q1.real + Q1_INICIAL
            q2 = acos((a**2+L3**2-b**2)/(2*a*L3)).real + Q2_INICIAL
            q3 = q2

            #Ajuste de las variables con valores MAX y MIN
            if q0 > Q0_MAX:
                q0 = Q0_MAX
            elif q0 < Q0_MIN:
                q0 = Q0_MIN
            
            if q1 > Q1_MAX:
                q1 = Q1_MAX
            elif q1 < Q1_MIN:
                q1 = Q1_MIN
            
            if q2 > Q2_MAX:
                q2 = Q2_MAX
            elif q2 < Q2_MIN:
                q2 = Q2_MIN

            #Agregado de las variables al vector a guardar
            q0v.append(round(q0*180/pi))
            q1v.append(round(q1*180/pi))
            q2v.append(round(q2*180/pi))
        
        except:
            print(f"No se puede alcanzar este punto: [{xC[i]}, {yC[i]}]")
            return 0
    

    q0v.extend(q0v[:-1])
    q1v.extend(q1v[:-1])
    q2v.extend(q2v[:-1])

    juntas = {
        'q0v' : q0v,
        'q1v' : q1v,
        'q2v' : q2v
    }

    with open(r'data/rutinas_py/parado.json', 'w+') as f:
        json.dump(juntas, f)  

    print("Listo!")      


#Entry point
if __name__ == '__main__':
    run()