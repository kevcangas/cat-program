import requests


#Envia la información contendia en lecturas a la página
def envio_datos(URL_SERVIDOR, PAGINA, lecturas, verbose = True):
    data = {
        'temperatura': lecturas[0],
        'gas_humo': lecturas[1],
        'presencia': lecturas[2],
        'luz': lecturas[3],
        'tacto': lecturas[4],
        'emocion': lecturas[5],
        'rutina': lecturas[6],
        'expresion': lecturas[7]
    }
    if verbose: print(data)
    requests.post(url= URL_SERVIDOR + PAGINA, json = data)


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
        requests.post(url = URL_SERVIDOR + PAGINA, json = data)
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
        requests.post(url = URL_SERVIDOR + PAGINA, json = data)
        #print(data)
        return True
    except:
        return False


#Entry point
if __name__ == '__main__':
    print('This is a module')