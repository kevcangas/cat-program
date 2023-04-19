#Librerías externas
import RPi.GPIO as GPIO
import time


#Librerías internas
from functions.LDR import *


def run():
    PIN_PIR = 4
    configuracion_LDR(PIN_PIR)

    for _ in range(30):
        if deteccion_luz:
            print("Se detectó luz")
        else:
            print("No se ha detectado luz")
        time.sleep(1)


if __name__ == '__main__':
    run()