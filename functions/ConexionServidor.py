#Librería para la conexión entre la raspberry y la app 


import requests

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


#Esta función envía las lecturas contenidas en una lista a la 
#url y pagina definida
def envio_datos(URL_SERVIDOR, PAGINA, lecturas):
    data = {
        'medicion1': lecturas[0],
        'medicion2': lecturas[1],
        'medicion3': lecturas[2],
        'medicion4': lecturas[3],
        'medicion5': lecturas[4],
        'medicion6': lecturas[5],
        'medicion7': lecturas[6],
        'medicion8': lecturas[7],
    }
    requests.post(URL_SERVIDOR + PAGINA, data)
    return