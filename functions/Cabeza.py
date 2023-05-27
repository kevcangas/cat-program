#python
import json
from math import pi
from time import sleep


#externas
from adafruit_servokit import ServoKit


def movCabeza(pca,
             rutina,
             CUELLO=8,
             CABEZA=9,
             BOCA=10,
             OREJAS=11
             ):
    
    if rutina == 0: #DEFAULT
        pca.servo[CUELLO].angle = 90
        pca.servo[CABEZA].angle = 115
        pca.servo[BOCA].angle = 130
        pca.servo[OREJAS].angle = 90
    
    elif rutina == 1: #SACUDIR CUELLO
        rutina_cuello = [90,135,90,45,90]
        # rutina_cuello.append(range(135,45))
        # rutina_cuello.append(range(45,90))

        for i in range(len(rutina_cuello)):
            pca.servo[CUELLO].angle = rutina_cuello[i]
            sleep(0.5)
        
        pca.servo[CABEZA].angle = 115
        pca.servo[BOCA].angle = 130
        pca.servo[OREJAS].angle = 90
    
    elif rutina == 2: #OREJAS
        pca.servo[CUELLO].angle = 90
        pca.servo[CABEZA].angle = 115
        pca.servo[BOCA].angle = 130

        rutina_orejas = [90,150,90]
        for i in range(len(rutina_orejas)):
            pca.servo[OREJAS].angle = rutina_orejas[i]
            sleep(0.5)
    
    elif rutina == 3: #BOCAS
        pca.servo[CUELLO].angle = 90
        pca.servo[CABEZA].angle = 115
        pca.servo[OREJAS].angle = 90

        rutina_boca = [90,130]
        for i in range(len(rutina_boca)):
            pca.servo[BOCA].angle = rutina_boca[i]
            sleep(0.5)