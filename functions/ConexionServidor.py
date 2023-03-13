#Librería para la conexión entre la raspberry y la app 

#Esta función recibe como parametros la información a enviar y 
#retorna un diccionario con los campos a llenar en la app movil
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

#Esta función solo envía un dato para el primer parametro de la app
#movil
def prueba_un_dato(dato):
    data = {
        'medicion1': dato,
    }
    return data