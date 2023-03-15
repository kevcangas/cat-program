import RPi.GPIO as GPIO

#Configura el pin a utilizar el sensor HW139
def configuracion_HW139(PIN_HW139):
    GPIO.setmode(GPIO.BCM) #REVISAR DOCUMENTACIÖN DE ADAFRUIT
    GPIO.setup(PIN_HW139, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#Esta función devuelve un True si se detecta una caricia
def deteccion_caricia(pin_sensor):
    touch = GPIO.input(pin_sensor)
    return touch