#Python
import time
import random


#Propias
from functions import Servomotores
from functions import Oled
from functions import ConexionServidor


#Información para el envio de datos
URL_SERVIDOR = 'http://10.104.121.41:80'
PAGINA_COMANDOS_REALIZADOS = "/control/gato/1/comandos/realizados/"


#Esta función realiza el movimiento de las extremidades
def rutinaControlada(tiempo_actual, 
                     tiempo_inicial, 
                     CONTROL_SERVOS, 
                     rutinas, 
                     rutina_aux, 
                     mov_activado,
                     IMAGENES,
                     imagenes_automatico,
                     oled1,
                     oled2,
                     expresion_aux,
                     comandos_realizados,
                     rutina_rostro,
                     automatico = True
                     ):


    #Activación automatica del movimiento y expresion
    if tiempo_actual - tiempo_inicial > 5 and automatico and mov_activado == False:
        
        #Selección automatica de rutinas y expresiones
        rutina_seleccionada = random.choice(rutinas)
        expresion_seleccionada = random.choice(imagenes_automatico)
        rutina_rostro_seleccionada = random.choice(rutina_rostro)

        print("Movimiento iniciado")
        
        #Mostrar expresion
        Oled.mostrar_imagen(IMAGENES[expresion_seleccionada], oled1, oled2)

        #Movimiento servomotores
        Servomotores.realizarRutinaP1(CONTROL_SERVOS, rutina_seleccionada)

        #Movimiento cabeza y cola
        Servomotores.movCabeza(CONTROL_SERVOS, rutina_rostro_seleccionada)

        mov_activado = True
        
        #Establecimiento del tiempo en que se activa el movimiento
        tiempo_inicial = time.time()

        return tiempo_inicial, rutina_seleccionada, mov_activado, expresion_seleccionada, comandos_realizados


    #Activación manual del movimiento y expresion
    if not automatico and mov_activado == False and comandos_realizados == False:

        #Establecimiento manual de la rutina y expresión
        rutina_seleccionada = rutina_aux
        expresion_seleccionada = expresion_aux

        print("Movimiento iniciado...")
        print(f"Rutina seleccionada: {rutina_seleccionada}")

        #Mostrar expresion
        Oled.mostrar_imagen(IMAGENES[expresion_seleccionada], oled1, oled2)

        #Movimiento servomotores
        Servomotores.realizarRutinaP1(CONTROL_SERVOS, rutina_seleccionada)
        mov_activado = True

        #Estblecimiento del tiempo en que se activa el movimiento
        tiempo_inicial = time.time()

        return tiempo_inicial, rutina_seleccionada, mov_activado, expresion_seleccionada, comandos_realizados
    

    #Desactivación del movimiento
    if tiempo_actual - tiempo_inicial > 10 and mov_activado == True:
        Servomotores.realizarRutinaP2(CONTROL_SERVOS, rutina_aux)
        mov_activado = False

        #Establece que el comando se realizó con exito
        comandos_realizados = 1

        #Establecimiento del tiempo en que se desactivo el movimiento
        tiempo_inicial = time.time()


        #Indica si se realizó el comando
        ConexionServidor.comunicacion_comandos_realizados(
            URL_SERVIDOR,
            PAGINA_COMANDOS_REALIZADOS,
            comandos_realizados
        )

        print("Movimiento terminado")
        print(f"Rutina seleccionada: {rutina_aux}")

        return tiempo_inicial, rutina_aux, mov_activado, expresion_aux, comandos_realizados

    
    return tiempo_inicial, rutina_aux, mov_activado, expresion_aux, comandos_realizados
    

#Entry point
if __name__ == "__main__":
    print("Es un modulo")