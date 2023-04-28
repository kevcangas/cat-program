#python
import time
import random
from math import pi


#externas
from mat4py import loadmat
from adafruit_servokit import ServoKit



def configuracion_servomotores():
    MIN_IMP = 500 #Pulso minimo para el servomotor
    MAX_IMP = 2500 #Pulso máximo para el servomotor
    MIN_ANG = 0 #Ángulo mínimo
    MAX_ANG = 120 #Ángulo máx

    nbPCAServo = 16
    pca = ServoKit(channels=16)

    for i in range(nbPCAServo):
        pca.servo[i].set_pulse_width_range(MIN_IMP, MAX_IMP)

    return pca


def cargar_rutina(id_mov):
    if(id_mov==0):
        PT = loadmat(r'data/rutinas/reposo_PT.mat')
        PD = loadmat(r'data/rutinas/reposo_PD.mat')
    elif(id_mov==1):
        PT = loadmat(r'data/rutinas/pie_PT.mat')
        PD = loadmat(r'data/rutinas/pie_PD.mat')
    elif(id_mov==2):
        PT = loadmat(r'data/rutinas/sentado_PT.mat')
        PD = loadmat(r'data/rutinas/sentado_PD.mat')
    elif(id_mov==3):
        PT = loadmat(r'data/rutinas/jugando_PT.mat')
        PD1 = loadmat(r'data/rutinas/jugando_PD1.mat')
        PD2 = loadmat(r'data/rutinas/jugando_PD2.mat')
        return PT,PD1,PD2

    elif(id_mov==4):
        PT = loadmat(r'data/rutinas/estirado_PT.mat')
        PD = loadmat(r'data/rutinas/estirado_PD.mat')
    elif(id_mov==5):
        PT = loadmat(r'data/rutinas/asustado_PT.mat')
        PD = loadmat(r'data/rutinas/asustado_PD.mat')
    elif(id_mov==6):
        PT = loadmat(r'data/rutinas/caminando_PT.mat')
        PD = loadmat(r'data/rutinas/caminando_PD.mat')
    
    return PT,PD 


def movPatas(pca,
             matT,
             matD,
             i=0,
             j=0,
             PATAT_1=[0,1,2],
             PATAT_2=[3,4,5],
             PATAD_1=[6,7,8],
             PATAD_2=[9,10,11]):
    
    #Pata trasera R 
    POSICION_SERVOS = [matT['q0v'][i], matT['q1v'][i], matT['q2v'][i]]
    for j in range(3):
        pass
        #print(round(POSICION_SERVOS[j]*180/pi)+45)
        #pca.servo[PATAT_1[j]].angle = round(POSICION_SERVOS[j]*180/pi)

    #Pata trasera L
    POSICION_SERVOS = [matT['q0v'][i], matT['q1v'][i], matT['q2v'][i]]
    for j in range(3):
        pass
        #print(round(POSICION_SERVOS[j]*180/pi)+45)
        #pca.servo[PATAT_2[j]].angle = round(POSICION_SERVOS[j]*180/pi)
    
    #Pata delantera R
    POSICION_SERVOS = [matD['q0v'][i], matD['q1v'][i], matD['q2v'][i]]
    for j in range(3):
        pass
        #print(round(POSICION_SERVOS[j]*180/pi)+45)
        #pca.servo[PATAD_1[j]].angle = round(POSICION_SERVOS[j]*180/pi)
    
    #Pata delantera L
    POSICION_SERVOS = [matD['q0v'][i], matD['q1v'][i], matD['q2v'][i]]
    for j in range(3):
        pass
        #print(round(POSICION_SERVOS[j]*180/pi)+45)
        #pca.servo[PATAD_2[j]].angle = round(POSICION_SERVOS[j]*180/pi)


#Realiza el movimiento de la primera mitad de la rutina
def realizarRutinaP1(pca, rutina_seleccionada):
    PT,PD = cargar_rutina(rutina_seleccionada)
    pasos_movimientos = len(PT['q0v'])
    control_pasos = pasos_movimientos//2-1

    for i in range(control_pasos):
        movPatas(pca, PT, PD, i, i)


#Esta función realiza el movimiento de la segunda mitad de la rutina
def realizarRutinaP2(pca, rutina_seleccionada):
    PT,PD = cargar_rutina(rutina_seleccionada)
    pasos_movimientos = len(PT['q0v'])
    control_pasos = pasos_movimientos//2-1

    for i in range(control_pasos, pasos_movimientos):
        movPatas(pca, PT, PD, i, i)