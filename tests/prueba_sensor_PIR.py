#Librerías externas
import RPi.GPIO as GPIO
import time


#Librerías internas
from functions.HCXX import *


def run():
    PIN_PIR = 27
    configuracion_HC(PIN_PIR)

    for _ in range(30):
        if deteccion_presencia:
            print("Se detectó presencia")
        else:
            print("No se ha detectado presencia")
        time.sleep(1)


if __name__ == '__main__':
    run()