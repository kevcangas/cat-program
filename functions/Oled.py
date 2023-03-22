from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from PIL import Image


#Función para configurar las pantallas
def configuracion_pantalla(port,address):
    serial = i2c(port, address) #port:usualmente 1 o 2 #address: dirección de la pantalla
    oled = ssd1306(serial)
    return oled


#Retorna una tupla con las imagenes cargadas donde la primera columna contiene
#las imagenes de la pantalla derecha y la segunda columna contiene
#las imagenes de la pantalla izquierda
def carga_imagenes():

    feliz_R = Image.open(r"data/expresiones/feliz_R.bmp")
    feliz_L = Image.open(r"data/expresiones/feliz_L.bmp")

    neutral_R = Image.open(r"data/expresiones/neutral_R.bmp")
    neutral_L = Image.open(r"data/expresiones/neutral_L.bmp")

    preocupado_R = Image.open(r"data/expresiones/preocupado_R.bmp")
    preocupado_L = Image.open(r"data/expresiones/preocupado_L.bmp")

    sueno_R = Image.open(r"data/expresiones/sueno_R.bmp")
    sueno_L = Image.open(r"data/expresiones/sueno_L.bmp")

    triste1_R = Image.open(r"data/expresiones/triste1_R.bmp")
    triste1_L = Image.open(r"data/expresiones/triste1_L.bmp")

    triste2_R = Image.open(r"data/expresiones/triste2_R.bmp")
    triste2_L = Image.open(r"data/expresiones/triste2_L.bmp")

    expresiones = ((feliz_R,feliz_L),(neutral_R,neutral_L),(preocupado_R,preocupado_L),
                (sueno_R,sueno_L),(triste1_R,triste1_L),(triste2_R,triste2_L))
    
    return expresiones


#Despliega las imagenes que se pasen en las pantallas
def mostrar_imagen(imagenes,oled1:ssd1306,oled2:ssd1306):
    oled1.clear()
    oled2.clear()
    oled1.display(imagenes[0])
    oled2.display(imagenes[1])
    return


#Realiza lo mismo que la función anterior pero con una pantalla
def mostrar_imagen_una_pantalla(imagenes,oled1:ssd1306):
    oled1.clear()
    oled1.display(imagenes[0])
    return