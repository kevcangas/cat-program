#python
import json
from math import pi


#externas
from adafruit_servokit import ServoKit


#Función para la configuración de los servomotores
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


#Función para la carga de rutinas
def cargar_rutina(id_mov):
    if(id_mov==0):
        with open(r'/home/gato/TT2/programa_gato/data/rutinas_py/reposo_PT.json') as f:
            PT = json.load(f)
        with open(r'/home/gato/TT2/programa_gato/data/rutinas_py/reposo_PD.json') as f:
            PD = json.load(f)

    elif(id_mov==1):
        with open(r'/home/gato/TT2/programa_gato/data/rutinas_py/pie_PT.json') as f:
            PT = json.load(f)
        with open(r'/home/gato/TT2/programa_gato/data/rutinas_py/pie_PD.json') as f:
            PD = json.load(f)

    elif(id_mov==2):
        with open(r'/home/gato/TT2/programa_gato/data/rutinas_py/sentado_PT.json') as f:
            PT = json.load(f)
        with open(r'/home/gato/TT2/programa_gato/data/rutinas_py/sentado_PD.json') as f:
            PD = json.load(f)

    elif(id_mov==3):
        with open(r'/home/gato/TT2/programa_gato/data/rutinas_py/jugando_PT.json') as f:
            PT = json.load(f)
        with open(r'/home/gato/TT2/programa_gato/data/rutinas_py/jugando_PD1.json') as f:
            PD1 = json.load(f)
        with open(r'/home/gato/TT2/programa_gato/data/rutinas_py/jugando_PD.json') as f:
            PD2 = json.load(f)

        return PT,PD1,PD2

    elif(id_mov==4):
        with open(r'/home/gato/TT2/programa_gato/data/rutinas_py/estirado_PT.json') as f:
            PT = json.load(f)
        with open(r'/home/gato/TT2/programa_gato/data/rutinas_py/estirado_PD.json') as f:
            PD = json.load(f)

    elif(id_mov==5):
        with open(r'/home/gato/TT2/programa_gato/data/rutinas_py/asustado_PT.json') as f:
            PT = json.load(f)
        with open(r'/home/gato/TT2/programa_gato/data/rutinas_py/asustado_PD.json') as f:
            PD = json.load(f)
    
    elif(id_mov==6):
        with open(r'/home/gato/TT2/programa_gato/data/rutinas_py/caminando_PT.json') as f:
            PT = json.load(f)
        with open(r'/home/gato/TT2/programa_gato/data/rutinas_py/caminando_PD.json') as f:
            PD = json.load(f)
    
    return PT,PD 


#Movimiento de una pata
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
        #print(POSICION_SERVOS[j])
        if j == 1:
            pca.servo[PATAT_1[j]].angle = POSICION_SERVOS[j]
        elif j == 2:
            pca.servo[PATAT_1[j]].angle = POSICION_SERVOS[j] + 16
        elif j == 0:
            pca.servo[PATAT_1[0]].angle = POSICION_SERVOS[j] - 1

    #Pata trasera L
    POSICION_SERVOS = [matT['q0v'][i], matT['q1v'][i], matT['q2v'][i]]
    for j in range(3):
        #print(POSICION_SERVOS[j])
        if j == 1:
            pca.servo[PATAT_2[j]].angle = 180 - POSICION_SERVOS[j] + 15
        elif j == 2:
            pca.servo[PATAT_2[j]].angle = 180 - POSICION_SERVOS[j]
        elif j == 0:
            pca.servo[PATAT_2[0]].angle = POSICION_SERVOS[j] + 12
    
    #Pata delantera R
    POSICION_SERVOS = [matD['q0v'][i], matD['q1v'][i], matD['q2v'][i]]
    for j in range(3):
        #print(POSICION_SERVOS[j])
        if j == 1:
            pca.servo[PATAD_1[j]].angle = POSICION_SERVOS[j] + 20
        elif j == 2:
            pca.servo[PATAD_1[j]].angle = POSICION_SERVOS[j]
        elif j == 0:
            pca.servo[PATAD_1[0]].angle = POSICION_SERVOS[j] 
        
    #Pata delantera L
    POSICION_SERVOS = [matD['q0v'][i], matD['q1v'][i], matD['q2v'][i]]
    for j in range(3):
        #print(POSICION_SERVOS[j])
        if j == 1:
            pca.servo[PATAD_2[j]].angle = 180 - POSICION_SERVOS[j] 
        elif j == 2:
            pca.servo[PATAD_2[j]].angle = 180 - POSICION_SERVOS[j]
        elif j == 0:
            pca.servo[PATAD_2[0]].angle = 180 - POSICION_SERVOS[j] + 6


#Realiza el movimiento de la primera mitad de la rutina
def realizarRutinaP1(pca, rutina_seleccionada):
    PT,PD = cargar_rutina(rutina_seleccionada)
    pasos_movimientos = len(PT['q0v'])
    control_pasos = pasos_movimientos//2-1

    for i in range(control_pasos):
        movPatas(pca, PT, PD, i, i)
        #sleep(0.02)


#Esta función realiza el movimiento de la segunda mitad de la rutina
def realizarRutinaP2(pca, rutina_seleccionada):
    PT,PD = cargar_rutina(rutina_seleccionada)
    pasos_movimientos = len(PT['q0v'])
    control_pasos = pasos_movimientos//2-1

    for i in range(control_pasos, pasos_movimientos):
        movPatas(pca, PT, PD, i, i)
        #sleep(0.02)