import RPi.GPIO as GPIO


#Configura el pin a utilizar el sensor HW139
def configuracion_HW139(PIN_HW139):
    GPIO.setmode(GPIO.BCM) #REVISAR DOCUMENTACIÖN DE ADAFRUIT (POR DEFECTO)
    GPIO.setup(PIN_HW139, GPIO.IN, pull_up_down = GPIO.PUD_UP)


#Esta función devuelve un True si se detecta una caricia
def deteccion_caricia(PIN_HW139):
    touch = GPIO.input(PIN_HW139)
    return int(touch)


#Entry point
if __name__ == '__main__':
    print('This is a module')