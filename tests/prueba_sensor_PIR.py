#Librerías externas
import RPi.GPIO as GPIO
import time


#Librerías internas
from functions.HCXX import *


def run():
    PIN_PIR = 27
    configuracion_HC(PIN_PIR)

    for i in range(30):
        print(f"Medición {i}: ")
        if deteccion_presencia(PIN_PIR):
            print("Se detectó presencia")
        else:
            print("No se ha detectado presencia")
        time.sleep(2)


if __name__ == '__main__':
    run()