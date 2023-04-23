import time
from math import pi
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
        PT = loadmat(r'rutinas\reposo_PT.mat')
        PD = loadmat(r'rutinas\reposo_PD.mat')
    elif(id_mov==1):
        PT = loadmat(r'rutinas\pie_PT.mat')
        PD = loadmat(r'rutinas\pie_PD.mat')
    elif(id_mov==2):
        PT = loadmat(r'rutinas\sentado_PT.mat')
        PD = loadmat(r'rutinas\sentado_PD.mat')
    elif(id_mov==3):
        PT = loadmat(r'rutinas\jugando_PT.mat')
        PD1 = loadmat(r'rutinas\jugando_PD1.mat')
        PD2 = loadmat(r'rutinas\jugando_PD2.mat')
        return PT,PD1,PD2

    elif(id_mov==4):
        PT = loadmat(r'rutinas\estirado_PT.mat')
        PD = loadmat(r'rutinas\estirado_PD.mat')
    elif(id_mov==5):
        PT = loadmat(r'rutinas\asustado_PT.mat')
        PD = loadmat(r'rutinas\asustado_PD.mat')
    elif(id_mov==6):
        PT = loadmat(r'rutinas\caminando_PT.mat')
        PD = loadmat(r'rutinas\caminando_PD.mat')
    
    return PT,PD 


def movPatas(pca,
             matT,
             matD,
             i,
             j,
             PATAT_1=[0,1,2],
             PATAT_2=[3,4,5],
             PATAD_1=[6,7,8],
             PATAD_2=[9,10,11]):
    
    #Pata trasera R 
    POSICION_SERVOS = [matT['q0v'][0][i], matT['q1v'][0][i], matT['q2v'][0][i]]
    for j,k in PATAT_1,POSICION_SERVOS:
        pca.servo[j].angle = k*pi/180

    #Pata trasera L
    POSICION_SERVOS = [matT['q0v'][0][i], matT['q1v'][0][i], matT['q2v'][0][i]]
    for j,k in PATAT_2,POSICION_SERVOS:
        pca.servo[j].angle = k*pi/180
    
    #Pata delantera R
    POSICION_SERVOS = [matD['q0v'][0][i], matD['q1v'][0][i], matD['q2v'][0][i]]
    for j,k in PATAD_1,POSICION_SERVOS:
        pca.servo[j].angle = k*pi/180
    
    #Pata delantera L
    POSICION_SERVOS = [matD['q0v'][0][i], matD['q1v'][0][i], matD['q2v'][0][i]]
    for j,k in PATAD_2,POSICION_SERVOS:
        pca.servo[j].angle = k*pi/180