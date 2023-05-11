#Python
from math import *
import json


#Librerías propias
from utils.calculo_juntas.obtener_trayectorias import obtener_trayectoria
from utils.calculo_juntas.calculo_juntas import calculo_juntas_PT, calculo_juntas_PD


def calculo_PT(rutina):

    #Creación de las listas con las trayectorias
    q0v=[]
    q1v=[]
    q2v=[]

    #Configuración fisica de las patas traseras
    Z0PT = 33.84
    L1PT = 100
    L2PT = 70
    L3PT = 60

    POSICION_SERVO_HOMBRO = 0

    #Posición inicial de las variables de junta (Radianes)    
    Q0_INICIAL_PT = 0
    Q1_INICIAL_PT = pi/2
    Q2_INICIAL_PT = 3*pi/2

    #Posiciones MAX y MIN
    Q0_MIN_PT = 0
    Q0_MAX_PT = 2*pi

    Q1_MIN_PT = 0
    Q1_MAX_PT = 2*pi
    
    Q2_MIN_PT = 0
    Q2_MAX_PT = 2*pi

    #Asignación de los puntos
    while 1:
        print("\033[;36m"+"Analsis PT"+'\033[0;m')
        xC, yC = obtener_trayectoria()
        seleccion = bool(input("Estas de acuerdo con la trayectoria?\n0 -> No\n1 -> Sí: "))
        if seleccion:
            break

    tamano = xC.size

    #Lectura de los puntos calculo de las juntas traseras
    for i in range(tamano):

        try:
            #Puntos a evaluar 
            x=xC[i]
            y=yC[i]
            z=0

            q0,q1,q2 = calculo_juntas_PT(
                            L1=L1PT,
                            L2=L2PT,
                            L3=L3PT,
                            Z0=Z0PT,
                            xC=x,
                            yC=y,
                            z=z,
                            POSICION_SERVO_HOMBRO=POSICION_SERVO_HOMBRO,
                            Q0_INICIAL=Q0_INICIAL_PT,
                            Q0_MIN=Q0_MIN_PT,
                            Q0_MAX=Q0_MAX_PT,
                            Q1_INICIAL=Q1_INICIAL_PT,
                            Q1_MIN=Q1_MIN_PT,
                            Q1_MAX=Q1_MAX_PT,
                            Q2_INICIAL=Q2_INICIAL_PT,
                            Q2_MIN=Q2_MIN_PT,
                            Q2_MAX=Q2_MAX_PT
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
    with open(r'data/rutinas_py/'+rutina+r'_PT.json', 'w+') as f:
        json.dump(juntas, f)  

    print("Calculo juntas traseras: Listo!")      


def calculo_PD(rutina):
    
    #Creación de las listas con las trayectorias
    q0v=[]
    q1v=[]
    q2v=[]

    #Configuración de las patas delanteras del robot
    Z0PD = 33.49
    Z1PD = 0
    L1PD = 100
    L2PD = 90

    POSICION_SERVO_HOMBRO = 0

    #Posición inicial de las variables de junta (Radianes)    
    Q0_INICIAL_PD = 0
    Q1_INICIAL_PD = pi/2
    Q2_INICIAL_PD = 3*pi/2

    #Posiciones MAX y MIN
    Q0_MIN_PD = 0
    Q0_MAX_PD = 2*pi

    Q1_MIN_PD = 0
    Q1_MAX_PD = 2*pi
    
    Q2_MIN_PD = 0
    Q2_MAX_PD = 2*pi

    #Asignación de los puntos
    while 1:
        print("\033[;36m"+"Analsis PD"+'\033[0;m')
        xC, yC = obtener_trayectoria()
        seleccion = bool(input("Estas de acuerdo con la trayectoria?\n0 -> No\n1 -> Sí: "))
        if seleccion:
            break

    tamano = xC.size

    for i in range(tamano):

        try:
            x=xC[i]
            y=yC[i]
            z=0

            q0,q1,q2 = calculo_juntas_PD(
                            L1=L1PD,
                            L2=L2PD,
                            Z0=Z0PD,
                            Z1=Z1PD,
                            xC=x,
                            yC=y,
                            z=z,
                            POSICION_SERVO_HOMBRO=POSICION_SERVO_HOMBRO,
                            Q0_INICIAL=Q0_INICIAL_PD,
                            Q0_MIN=Q0_MIN_PD,
                            Q0_MAX=Q0_MAX_PD,
                            Q1_INICIAL=Q1_INICIAL_PD,
                            Q1_MIN=Q1_MIN_PD,
                            Q1_MAX=Q1_MAX_PD,
                            Q2_INICIAL=Q2_INICIAL_PD,
                            Q2_MIN=Q2_MIN_PD,
                            Q2_MAX=Q2_MAX_PD
                        )
            #Agregado de las variables al vector a guardar
            q0v.append(q0)
            q1v.append(q1)
            q2v.append(q2)
        
        except ValueError as ve:
            print(f"No se puede alcanzar este punto: [{xC[i]}, {yC[i]}]")
            print(ve)
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
    with open(r'data/rutinas_py/'+rutina+r'_PD.json', 'w+') as f:
        json.dump(juntas, f)  

    print("Calculo juntas delanteras: Listo!") 


#Programa principal
def run():
    rutina = input("Introduce la rutina que es: ")
    calculo_PT(rutina)
    calculo_PD(rutina)


#Entry point
if __name__ == '__main__':
    run()