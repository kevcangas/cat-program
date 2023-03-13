#PRUEBA1: ENVIO DE DATOS LEIDOS A LA APP MOVIL


#LIBRERIAS EXTERNAS
import time
import adafruit_dht
import requests


#LIBRERIAS LOCALES
from functions.ConexionServidor import prueba_un_dato
from functions.DHT11 import lectura_temperatura


#INFORMACION PARA LA APP MOVIL
URL_SERVIDOR = 'http://192.168.1.198:80'
PAGINA = "/control/1/lectura_medicion/"


#INFORMACION PARA LA LECTURA DE LA TEMPERATURA
PIN_DHT = 23
DHT = adafruit_dht.DHT11(PIN_DHT)


#PROGRAMA PRINCIPAL
def run():
    temperatura = lectura_temperatura(DHT)
    requests.post(URL_SERVIDOR + PAGINA, prueba_un_dato(temperatura))
    time.sleep(10)


if __name__ == '__main__':
    for _ in range(10):
        run()