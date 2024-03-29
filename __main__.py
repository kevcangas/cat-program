#python
import subprocess
import time


#OpenCV2
import cv2


#Librerías propias
from functions import audio
from functions import ConexionServidor
from functions import DeteccionExpresionesRasp as DER
from functions import DHT11
from functions import HCXX
from functions import HW139
from functions import LDR
from functions import MQ2
from functions import Oled
from functions import Servomotores
from functions import FuncionesPrincipales as FP


#Programa principal
def run():

    #Inilización de los actuadores y establecimiento de las conexiones
    
    #PAGINAS PARA EL ENVIO Y RECEPCIÓN DE DATOS
    URL_SERVIDOR = 'http://192.168.1.198:80'
    PAGINA_ENV = "/control/gato/1/mediciones/actualizacion/automatico/"
    PAGINA_REC = "/control/gato/1/comandos/lectura/"
    PAGINA_ENCENDIDO = "/control/gato/1/comandos/actualizacion/"
    ConexionServidor.comunicacion_encendido(URL_SERVIDOR, PAGINA_ENCENDIDO)
    print("Conexion internet: Listo")


    #INICIALIZACION RED NEURONAL Y CAMARA
    cap = cv2.VideoCapture(0)
    DETECTOR_ROSTRO = DER.cargar_Cascade()
    RED_CONVOLUCIONAL = DER.cargar_CNN()
    etiqueta_expresion = 0
    print("Iniciación neurona: Listo")


    #CONFIGURACIÓN PANTALLA Y CARGA DE IMAGENES A LA MEMORIA
    IMAGENES = Oled.carga_imagenes()
    OLED_1 = Oled.configuracion_pantalla(1, 0x3D)
    OLED_2 = Oled.configuracion_pantalla(1, 0x3C)
    #Expresiones extablecidas para cada expresión detectada
    EXPRESIONES_NEUTRAL = [2, 4]
    EXPRESIONES_FELICIDAD = [1]
    EXPRESIONES_ENOJO = [1,3]
    EXPRESIONES_TRISTEZA = [1,5]
    #Expresiión inicial
    expresion = 0
    expresion_manual = 0
    Oled.mostrar_imagen(IMAGENES[expresion], OLED_1, OLED_2)
    print("Configuracion pantallas: Listo")


    #CONFIGURACIÓN SENSOR DHT11
    PIN_DHT = 22
    DHT = DHT11.configuracion_DHT11(PIN_DHT)
    temp_inicial = 0
    print("Configuracion DHT11: Listo")


    #CONFIGURACIÓN SENSOR HCXX
    PIN_PIR = 27
    HCXX.configuracion_HC(PIN_PIR)
    print("Configuracion HCXX: Listo")


    #CONFIGURACIÓN SENSOR HW139
    PIN_HW139_1 = 17
    HW139.configuracion_HW139(PIN_HW139_1)
    PIN_HW139_2 = 23
    HW139.configuracion_HW139(PIN_HW139_2)
    PIN_HW139_3 = 24
    HW139.configuracion_HW139(PIN_HW139_3)
    PIN_HW139_4 = 25
    HW139.configuracion_HW139(PIN_HW139_4)
    print("Configuracion HW139: Listo")

    
    #CONFIGURACIÓN SENSOR LDR
    PIN_LDR = 4
    LDR.configuracion_LDR(PIN_LDR)
    print("Configuracion LDR: Listo")


    #CONFIGURACIÓN SENSOR MQ2
    SENSOR_HUMO = MQ2.configuracion_MQ2()
    print("Configuración sensor humo: Listo")


    #CONFIGURACIÓN SERVOMOTORES
    CONTROL_SERVOS = Servomotores.configuracion_servomotores()
    rutina = 0
    #Posición inicial
    PT, PD =  Servomotores.cargar_rutina(rutina)
    Servomotores.movPatas(CONTROL_SERVOS,PT,PD)
    #Rutinas
    RUTINAS_NEUTRAL = [0, 1, 2, 4, 6]
    RUTINAS_FELICIDAD = [1, 3]
    RUTINAS_ENOJO = [2, 5]
    RUTINAS_TRISTEZA = [0, 1 ,2] 
    #Variables de control
    mov_activado = False
    tiempo_inicial = time.time()
    rutina_manual = 0
    automatico = 1
    comandos_realizados = 1
    print("Configuración servomotores: Listo")


    #Espera del programa
    time.sleep(3)
    print("Corriendo programa principal")


    #Programa principal de ejecución
    while True:

        #Lectura de la aplicación movil
        data_recibida = ConexionServidor.recepcion_datos(URL_SERVIDOR, PAGINA_REC)
        
        automatico = data_recibida['automatico']

        #si no está en automatico, lee las rutinas y expresiones de la app
        if not automatico:
            rutina_manual = data_recibida['rutina_manual']
            expresion_manual = data_recibida['expresion_manual']
            comandos_realizados = data_recibida['comandos_realizados']
        
        encendido = data_recibida['encendido']


        #Lectura de sensores
        temperatura = DHT11.lectura_temperatura(DHT, temp_inicial)
        temp_inicial = temperatura
        gas_humo = 1 if MQ2.medicion_gas(SENSOR_HUMO) > 3 else 0
        presencia = HCXX.deteccion_presencia(PIN_PIR)
        luz = LDR.deteccion_luz(PIN_LDR)
        tacto = (HW139.deteccion_caricia(PIN_HW139_1) or 
                 HW139.deteccion_caricia(PIN_HW139_2) or
                 HW139.deteccion_caricia(PIN_HW139_3) or
                 HW139.deteccion_caricia(PIN_HW139_4) )


        #Lectura de las expresiones
        try:
            expresiones_aux = []
            for _ in range(5):
                expresiones_aux.append(DER.deteccion_expresiones(
                                        cap,
                                        DETECTOR_ROSTRO, 
                                        RED_CONVOLUCIONAL, 
                                        verbose=True, 
                                        mostrar_ima=False
                                        ))
            
            etiqueta_expresion = max(set(expresiones_aux), key=expresiones_aux.count)

        except ValueError as ve:
            print(ve)

        
        #Envio de las lecturas al servidor
        ConexionServidor.envio_datos(
            URL_SERVIDOR,
            PAGINA_ENV,
            [temperatura, 
             gas_humo,
             presencia,
             luz,
             tacto,
             etiqueta_expresion,
             rutina,
             expresion]
        )


        #Toma de decisión si se apaga
        if not encendido:
            subprocess.run("sudo shutdown -h now", shell=True)
        
        #Selección de rutina automaticamente
        tiempo_actual = time.time()

        if automatico:
        
            #Acciones automaticas si se detecta presencia
            if presencia:
                #Detección expresión enojo
                if etiqueta_expresion == 0:

                    tiempo_inicial , rutina, mov_activado, expresion, comandos_realizados = FP.rutinaControlada(
                        tiempo_actual = tiempo_actual, 
                        tiempo_inicial = tiempo_inicial, 
                        CONTROL_SERVOS = CONTROL_SERVOS, 
                        rutinas = RUTINAS_ENOJO,
                        rutina_aux = rutina, 
                        mov_activado = mov_activado,
                        IMAGENES = IMAGENES,
                        imagenes_automatico = EXPRESIONES_ENOJO,
                        oled1 = OLED_1,
                        oled2 = OLED_2,
                        expresion_aux = expresion,
                        comandos_realizados = comandos_realizados,
                        automatico = True
                        )

                #Detección expresión felicidad
                elif etiqueta_expresion == 1:
                    
                    tiempo_inicial , rutina, mov_activado, expresion, comandos_realizados = FP.rutinaControlada(
                        tiempo_actual = tiempo_actual, 
                        tiempo_inicial = tiempo_inicial, 
                        CONTROL_SERVOS = CONTROL_SERVOS, 
                        rutinas = RUTINAS_FELICIDAD,
                        rutina_aux = rutina, 
                        mov_activado = mov_activado,
                        IMAGENES = IMAGENES,
                        imagenes_automatico = EXPRESIONES_FELICIDAD,
                        oled1 = OLED_1,
                        oled2 = OLED_2,
                        expresion_aux = expresion,
                        comandos_realizados = comandos_realizados,
                        automatico = True
                        )
                    
                #Detección expresión neutra
                elif etiqueta_expresion == 2:
                    
                    tiempo_inicial , rutina, mov_activado, expresion, comandos_realizados = FP.rutinaControlada(
                        tiempo_actual = tiempo_actual, 
                        tiempo_inicial = tiempo_inicial, 
                        CONTROL_SERVOS = CONTROL_SERVOS, 
                        rutinas = RUTINAS_NEUTRAL,
                        rutina_aux = rutina, 
                        mov_activado = mov_activado,
                        IMAGENES = IMAGENES,
                        imagenes_automatico = EXPRESIONES_NEUTRAL,
                        oled1 = OLED_1,
                        oled2 = OLED_2,
                        expresion_aux = expresion,
                        comandos_realizados = comandos_realizados,
                        automatico = True
                        )
                    
                #Detección expresión tristeza
                elif etiqueta_expresion == 3:
                    
                    tiempo_inicial , rutina, mov_activado, expresion, comandos_realizados = FP.rutinaControlada(
                        tiempo_actual = tiempo_actual, 
                        tiempo_inicial = tiempo_inicial, 
                        CONTROL_SERVOS = CONTROL_SERVOS, 
                        rutinas = RUTINAS_TRISTEZA,
                        rutina_aux = rutina, 
                        mov_activado = mov_activado,
                        IMAGENES = IMAGENES,
                        comandos_realizados = comandos_realizados,
                        imagenes_automatico = EXPRESIONES_TRISTEZA,
                        oled1 = OLED_1,
                        oled2 = OLED_2,
                        expresion_aux = expresion,
                        automatico = True
                        )
                    
                else:

                    tiempo_inicial , rutina, mov_activado, expresion, comandos_realizados = FP.rutinaControlada(
                        tiempo_actual = tiempo_actual, 
                        tiempo_inicial = tiempo_inicial, 
                        CONTROL_SERVOS = CONTROL_SERVOS, 
                        rutinas = [0],
                        rutina_aux = rutina, 
                        mov_activado = mov_activado,
                        IMAGENES = IMAGENES,
                        comandos_realizados = comandos_realizados,
                        imagenes_automatico = [0],
                        oled1 = OLED_1,
                        oled2 = OLED_2,
                        expresion_aux = expresion,
                        automatico = True
                        )
            
            #Si no se detecta presencia
            else:

                if tiempo_actual - tiempo_inicial > 300:
                    audio.reproducir_audio()
                    tiempo_inicial = time.time()


        #Selección de rutina manual
        else:
            
            tiempo_inicial , rutina, mov_activado, expresion, comandos_realizados = FP.rutinaControlada(
                tiempo_actual = tiempo_actual, 
                tiempo_inicial = tiempo_inicial, 
                CONTROL_SERVOS = CONTROL_SERVOS, 
                rutinas = [],
                rutina_aux = rutina_manual, 
                mov_activado = mov_activado,
                IMAGENES = IMAGENES,
                imagenes_automatico = [],
                oled1 = OLED_1,
                oled2 = OLED_2,
                expresion_aux = expresion_manual,
                comandos_realizados = comandos_realizados,
                automatico = False
                )
            
            

#Entry point
if __name__ == '__main__':
    run()