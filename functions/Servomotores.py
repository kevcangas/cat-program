#python
import json
from math import pi
from time import sleep

#externas
from adafruit_servokit import ServoKit


#Internas
from functions import audio


#Función para la configuración de los servomotores
def configuracion_servomotores(address):
    MIN_IMP = 500 #Pulso minimo para el servomotor
    MAX_IMP = 2500 #Pulso máximo para el servomotor
    MIN_ANG = 0 #Ángulo mínimo
    MAX_ANG = 120 #Ángulo máx

    nbPCAServo = 16
    pca = ServoKit(channels=16, address=address)

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
        with open(r'/home/gato/TT2/programa_gato/data/rutinas_py/jugando_PD2.json') as f:
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
        with open(r'/home/gato/TT2/programa_gato/data/rutinas_py/caminar_PT.json') as f:
            PT = json.load(f)
        with open(r'/home/gato/TT2/programa_gato/data/rutinas_py/caminar_PD.json') as f:
            PD = json.load(f)
    
    return PT,PD 


#Movimiento de una pata
def movPatas(pca1,
             matT,
             matD,
             i=0,
             k=0,
             PATAT_1=[0,1],
             PATAT_2=[2,3],
             PATAD_1=[4,5],
             PATAD_2=[6,7],
             pca2 = None):
    
    if pca2 == None:
        pca2 = pca1
    
    if len(matT) == 1:
        matT=matT[0]
        #Pata trasera R 
        POSICION_SERVOS = [matT['q0v'][i], matT['q1v'][i], matT['q2v'][i]]
        for j in range(2):
            if j == 0:
                pca1.servo[PATAT_1[j]].angle = POSICION_SERVOS[j+1] - 25
            elif j == 1:
                pca1.servo[PATAT_1[j]].angle = POSICION_SERVOS[j+1] - 5

        #Pata trasera L
        POSICION_SERVOS = [matT['q0v'][k], matT['q1v'][k], matT['q2v'][k]]
        for j in range(2):
            if j == 0:
                pca1.servo[PATAT_2[j]].angle = 180 - POSICION_SERVOS[j+1] + 5
            elif j == 1:
                pca1.servo[PATAT_2[j]].angle = 180 - POSICION_SERVOS[j+1] - 50
    else:
        matT1 = matT[0]
        matT2 = matT[1]
        #Pata trasera R 
        POSICION_SERVOS = [matT1['q0v'][i], matT1['q1v'][i], matT1['q2v'][i]]
        for j in range(2):
            if j == 0:
                pca1.servo[PATAT_1[j]].angle = POSICION_SERVOS[j+1] - 25
            elif j == 1:
                pca1.servo[PATAT_1[j]].angle = POSICION_SERVOS[j+1] - 5

        #Pata trasera L
        POSICION_SERVOS = [matT2['q0v'][k], matT2['q1v'][k], matT2['q2v'][k]]
        for j in range(2):
            if j == 0:
                pca1.servo[PATAT_2[j]].angle = 180 - POSICION_SERVOS[j+1] + 5
            elif j == 1:
                pca1.servo[PATAT_2[j]].angle = 180 - POSICION_SERVOS[j+1] - 50
        
    #Patas delanteras
    if len(matD) == 1:
        matD=matD[0]
        #Pata delantera R
        POSICION_SERVOS = [matD['q0v'][k], matD['q1v'][k], matD['q2v'][k]]
        for j in range(2):
            if j == 0:
                pca2.servo[PATAD_1[j]].angle = POSICION_SERVOS[j+1] - 23
            elif j == 1:
                pca2.servo[PATAD_1[j]].angle = POSICION_SERVOS[j+1] - 15
            
        #Pata delantera L
        POSICION_SERVOS = [matD['q0v'][i], matD['q1v'][i], matD['q2v'][i]]
        for j in range(2):
            if j == 0:
                pca2.servo[PATAD_2[j]].angle = 180 - POSICION_SERVOS[j+1] + 8
            elif j == 1:
                pca2.servo[PATAD_2[j]].angle = 180 - POSICION_SERVOS[j+1] + 5
         
    else:
        matD1 = matD[0]
        matD2 = matD[1]
        #Pata delantera R
        POSICION_SERVOS = [matD1['q0v'][k], matD1['q1v'][k], matD1['q2v'][k]]
        for j in range(2):
            if j == 0:
                pca2.servo[PATAD_1[j]].angle = POSICION_SERVOS[j+1] - 23
            elif j == 1:
                pca2.servo[PATAD_1[j]].angle = POSICION_SERVOS[j+1] - 15
            
        #Pata delantera L
        POSICION_SERVOS = [matD2['q0v'][i], matD2['q1v'][i], matD2['q2v'][i]]
        for j in range(2):
            if j == 0:
                pca2.servo[PATAD_2[j]].angle = 180 - POSICION_SERVOS[j+1] + 8
            elif j == 1:
                pca2.servo[PATAD_2[j]].angle = 180 - POSICION_SERVOS[j+1] + 5


#Realiza el movimiento de la primera mitad de la rutina
def realizarRutinaP1(pca1,rutina_seleccionada, pca2 = None):
    if pca2 == None:
        pca2 = pca1

    if rutina_seleccionada != 3:
        PT,PD = cargar_rutina(rutina_seleccionada)
        pasos_movimientos = len(PT['q0v'])
        control_pasos = pasos_movimientos//2-1

        for i in range(control_pasos):
            movPatas(pca1,pca2, [PT], [PD], i, i)
            #sleep(0.02)
    
    else:
        PT,PD1,PD2 = cargar_rutina(rutina_seleccionada)
        pasos_movimientos = len(PT['q0v'])
        control_pasos = pasos_movimientos//2-1

        for i in range(control_pasos):
            movPatas(pca1,pca2, [PT], [PD1,PD2], i, i)
            #sleep(0.02)


#Esta función realiza el movimiento de la segunda mitad de la rutina
def realizarRutinaP2(pca1, rutina_seleccionada, pca2=None):
    if pca2 == None:
        pca2 = pca1

    if rutina_seleccionada != 3:
        PT,PD = cargar_rutina(rutina_seleccionada)
        pasos_movimientos = len(PT['q0v'])
        control_pasos = pasos_movimientos//2-1

        for i in range(control_pasos, pasos_movimientos):
            movPatas(pca1,pca2, [PT], [PD], i, i)
            #sleep(0.02)
    
    else:
        PT,PD1, PD2 = cargar_rutina(rutina_seleccionada)
        pasos_movimientos = len(PT['q0v'])
        control_pasos = pasos_movimientos//2-1

        for i in range(control_pasos, pasos_movimientos):
            movPatas(pca1,pca2, [PT], [PD1,PD2], i, i)
            #sleep(0.02)


#Rutina de caminar
def caminar(pca1, pca2=None, rutina_seleccionada=6):
    if pca2 == None:
        pca2 = pca1
        
    PT,PD = cargar_rutina(rutina_seleccionada)
    pasos_movimientos = len(PT['q0v'])
    control_pasos = pasos_movimientos//2-1

    i = 0
    j = 50
    for _ in range(control_pasos):
        movPatas(pca1,pca2, [PT], [PD], i=i, k=j)
        i+=1
        j+=1
        if j == control_pasos:
            j = 0
        

#Movimeinto de la cabeza 
def movCabeza(pca,
             rutina,
             CUELLO=8,
             CABEZA=9,
             BOCA=10,
             OREJAS=11
             ):
    

    #Default
    if rutina == 0: 
        pca.servo[CUELLO].angle = 90
        pca.servo[CABEZA].angle = 115
        pca.servo[BOCA].angle = 130
        pca.servo[OREJAS].angle = 90
    

    #Sacudir cuello
    elif rutina == 1: 
        rutina_cuello = [90,135,90,45,90]
        for i in rutina_cuello:
            pca.servo[CUELLO].angle = i
            sleep(0.5)
        
        pca.servo[CABEZA].angle = 115
        pca.servo[BOCA].angle = 130
        pca.servo[OREJAS].angle = 90
    

    #Movimiento orejas
    elif rutina == 2: 
        pca.servo[CUELLO].angle = 90
        pca.servo[CABEZA].angle = 115
        pca.servo[BOCA].angle = 130

        rutina_orejas = [100,0,100]
        for i in rutina_orejas:
            pca.servo[OREJAS].angle = i
            sleep(0.5)
    

    #Movimiento boca y maullido
    elif rutina == 3: 
        pca.servo[CUELLO].angle = 90
        pca.servo[CABEZA].angle = 115
        pca.servo[OREJAS].angle = 90

        rutina_boca = [90,130,90]
        for j,i in enumerate(rutina_boca):
            pca.servo[BOCA].angle = i
            sleep(0.5)
            if j == 1:
                audio.reproducir_audio()
    
    #Movimeinto cabeza arriba
    elif rutina == 4:
        pca.servo[CUELLO].angle = 90
        pca.servo[BOCA].angle = 130
        pca.servo[OREJAS].angle = 90

        rutina_cabeza = [115, 165, 115]
        for i in rutina_cabeza:
            pca.servo[CABEZA].angle = i
            sleep(0.5)
    
    #Movimeinto cabeza abajo
    elif rutina == 5:
        pca.servo[CUELLO].angle = 90
        pca.servo[BOCA].angle = 130
        pca.servo[OREJAS].angle = 90

        rutina_cabeza = [115, 75, 115]
        for i in rutina_cabeza:
            pca.servo[CABEZA].angle = i
            sleep(0.5)
        

#Función para el movimiento de la cola
def movCola(pca,COLA=12):
    pca.servo[COLA].angle = 90
    sleep(0.1)
    pca.servo[COLA].angle = 180
