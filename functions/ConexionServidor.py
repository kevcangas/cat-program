#Librería para la conexión entre la raspberry y la app 

def data_a_enviar(d1,d2,d3,d4,d5,d6,d7,d8):
    data = {
        'medicion1': d1,
        'medicion2': d2,
        'medicion3': d3,
        'medicion4': d4,
        'medicion5': d5,
        'medicion6': d6,
        'medicion7': d7,
        'medicion8': d8,
    }
    return data