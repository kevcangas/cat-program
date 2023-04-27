#Librería para la lectura de temperatura y humedad
import adafruit_dht


def configuracion_DHT11(DHT_PIN):
    return adafruit_dht.DHT11(DHT_PIN)


#Esta función entrega la temepratura y humedad detectada
def lectura_temperatura_humedad(DHT, temperatura):
    try:
        temperatura = DHT.temperature
        humedad = DHT.humidity
    except RuntimeError:
        return temperatura
    return temperatura, humedad


#Esta función entrega la temperatura del sensor
def lectura_temperatura(DHT, temperatura_inicial):
    try:
        temperatura = DHT.temperature
        return temperatura
    except RuntimeError:
        return temperatura_inicial
    

#Esta función entrega la humedad detectada
def lectura_humedad(DHT):
    humedad = DHT.humidity
    return humedad


#Entry point
if __name__ == '__main__':
    print('This is a module')