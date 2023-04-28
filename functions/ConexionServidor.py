import requests


#Envia la información contendia en lecturas a la página
def envio_datos(URL_SERVIDOR, PAGINA, lecturas, verbose = False):
    data = {
        'medicion1': lecturas[0],
        'medicion2': lecturas[1],
        'medicion3': lecturas[2],
        'medicion4': lecturas[3],
        'medicion5': lecturas[4],
        'medicion6': lecturas[5],
        'medicion7': lecturas[6],
        'medicion8': lecturas[7]
    }
    if verbose: print(data)
    requests.post(URL_SERVIDOR + PAGINA, data)


#Regresa un diccionario con la información recibida de la página
def recepcion_datos(URL_SERVIDOR, PAGINA_REC):
    try:
        response = requests.get(URL_SERVIDOR + PAGINA_REC)
        return response.json()
    except:
        return False


#Lee el comando de encendido o apagado
def lectura_encendido(URL_SERVIDOR, PAGINA):
    try:
        response = requests.get(URL_SERVIDOR + PAGINA)
        return response.json()
    except:
        return False
    

#Coloca el encendido del gato en la base de datos
def comunicacion_encendido(URL_SERVIDOR, PAGINA):
    data = {
        "encendido": 1,
        "rutina_manual": 0,
        "expresion_manual": 0,
        "automatico": 1,
        "comandos_realizados": 1
    }
    try:
        requests.post(URL_SERVIDOR + PAGINA, data)
        #print(data)
        return True
    except:
        return False


#Coloca el encendido del gato en la base de datos
def comunicacion_comandos_realizados(URL_SERVIDOR, PAGINA, realizado):
    data = {
        "comandos_realizados": int(realizado)
    }
    try:
        requests.post(URL_SERVIDOR + PAGINA, data)
        #print(data)
        return True
    except:
        return False


#Entry point
if __name__ == '__main__':
    print('This is a module')