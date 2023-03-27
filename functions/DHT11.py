#Librería para la lectura de temperatura y humedad

def lectura_temperatura_humedad(DHT, temperatura):
    try:
        temperatura = DHT.temperature
        humedad = DHT.humidity
    except RuntimeError:
        return temperatura
    return temperatura, humedad


def lectura_temperatura(DHT, temperatura_inicial):
    try:
        temperatura = DHT.temperature
        return temperatura
    except RuntimeError:
        return temperatura_inicial
    


def lectura_humedad(DHT):
    humedad = DHT.humidity
    return humedad