#Python
from math import *
import json


#Librerías propias
from utils.calculo_juntas.obtener_trayectorias import obtener_trayectoria
from utils.calculo_juntas.calculo_juntas import calculo_juntas_PT


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

            q0,q1,q2 = calculo_juntas_PT(
                            L1=L1,
                            L2=L2,
                            L3=L3,
                            Z0=Z0,
                            xC=x,
                            yC=y,
                            z=z,
                            POSICION_SERVO_HOMBRO=POSICION_SERVO_HOMBRO,
                            Q0_INICIAL=Q0_INICIAL,
                            Q0_MIN=Q0_MIN,
                            Q0_MAX=Q0_MAX,
                            Q1_INICIAL=Q1_INICIAL,
                            Q1_MIN=Q1_MIN,
                            Q1_MAX=Q1_MAX,
                            Q2_INICIAL=Q2_INICIAL,
                            Q2_MIN=Q2_MIN,
                            Q2_MAX=Q2_MAX
                        )

            #Agregado de las variables al vector a guardar
            q0v.append(q0)
            q1v.append(q1)
            q2v.append(q2)
        
        except:
            print(f"No se puede alcanzar este punto: [{xC[i]}, {yC[i]}]")
            return 0
    
    #Duplicado de la trayectoria en espejo
    q0v.extend(q0v[:-1])
    q1v.extend(q1v[:-1])
    q2v.extend(q2v[:-1])

    #Creación de JSON para su facil acceso
    juntas = {
        'q0v' : q0v,
        'q1v' : q1v,
        'q2v' : q2v
    }

    #Guardado del archivo JSON
    with open(r'data/rutinas_py/reposo_PT.json', 'w+') as f:
        json.dump(juntas, f)  

    print("Listo!")      


#Entry point
if __name__ == '__main__':
    run()