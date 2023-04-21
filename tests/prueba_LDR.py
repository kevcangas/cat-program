#Librerías externas
import RPi.GPIO as GPIO
import time


#Librerías internas
from functions.LDR import *


def run():
    PIN_PIR = 4
    configuracion_LDR(PIN_PIR)

    for i in range(30):
        print(f"Medición {i}: ")
        if deteccion_luz(PIN_PIR):
            print("Se detectó luz")
        else:
            print("No se ha detectado luz")
        time.sleep(1)


if __name__ == '__main__':
    run()