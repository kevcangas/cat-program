import RPi.GPIO as GPIO


#Configura el pin a utilizar para el sensor 
def configuracion_LDR(PIN_LDR):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_LDR, GPIO.IN)


#Devuelve un true si detecta presencia
def deteccion_luz(PIN_LDR):
    luz = not GPIO.input(PIN_LDR)
    return luz


#Entry point
if __name__ == '__main__':
    print('This is a module')