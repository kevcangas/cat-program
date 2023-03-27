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
        'medicion8': lecturas[7],
        'medicion9': lecturas[8]
    }
    if verbose: print(data)
    requests.post(URL_SERVIDOR + PAGINA, data)
    return


#Regresa un diccionario con la información recibida de la página
def recepcion_datos(URL_SERVIDOR, PAGINA_REC):
    response = requests.get(URL_SERVIDOR + PAGINA_REC)
    return response.json()
