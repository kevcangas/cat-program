import RPi.GPIO as GPIO
import time


#Configura el pin a utilizar para el sensor 
def configuracion_HC(PIN_PIR):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_PIR, GPIO.IN)


#Devuelve un true si detecta presencia
def deteccion_presencia(PIN_PIR):
    presencia = GPIO.input(PIN_PIR)
    return int(presencia)


#Entry point
if __name__ == '__main__':
    print('This is a module')