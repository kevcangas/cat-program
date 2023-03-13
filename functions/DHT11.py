#Librería para la lectura de temperatura y humedad

def lectura_temperatura_humedad(DHT):
    temperatura = DHT.temperature
    humedad = DHT.humidity
    return temperatura, humedad


def lectura_temperatura(DHT):
    temperatura = DHT.temperature
    return temperatura


def lectura_humedad(DHT):
    humedad = DHT.humidity
    return humedad