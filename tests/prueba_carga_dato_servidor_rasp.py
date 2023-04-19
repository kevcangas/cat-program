#PRUEBA1: ENVIO DE DATOS LEIDOS A LA APP MOVIL


#LIBRERIAS EXTERNAS
import time
import adafruit_dht


#LIBRERIAS LOCALES
from functions.ConexionServidor import envio_datos
from functions.DHT11 import lectura_temperatura
import functions.HW139 as sensor_touch


#PROGRAMA PRINCIPAL
def run():

    #INFORMACION PARA LA APP MOVIL
    URL_SERVIDOR = 'http://169.254.2.167:80/'
    PAGINA = "/control/1/lectura_medicion/"


    #INFORMACION PARA LA LECTURA DE LA TEMPERATURA
    PIN_DHT = 22
    DHT = adafruit_dht.DHT11(PIN_DHT)
    temp_inicial = 0


    #INFORMACIÖN PARA EL SENSOR HW139
    PIN_HW139 = 17
    sensor_touch.configuracion_HW139(PIN_HW139)

    for _ in range(20):
        temperatura = lectura_temperatura(DHT, temp_inicial)
        temp_inicial = temperatura
        d2 = 0
        d3 = 0
        d4 = 1
        d5 = sensor_touch.deteccion_caricia(PIN_HW139)
        d6 = 4
        d7 = 0
        d8 = 1
        d9 = 0
        envio_datos(URL_SERVIDOR, PAGINA, [temperatura,d2,d3,d4,d5,d6,d7,d8,d9])
        print('Envio correcto de datos')
        time.sleep(1)


#Entry point
if __name__ == '__main__':
    run()