#Python
import time
import random


#Propias
from functions import Servomotores
from functions import Oled


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
                     automatico = True
                     ):


    #Activación automatica del movimiento y expresion
    if tiempo_actual - tiempo_inicial > 120 and automatico and mov_activado == False:
        
        #Selección automatica de rutinas y expresiones
        rutina_seleccionada = random.choice(rutinas)
        expresion_seleccionada = random.choice(imagenes_automatico)
        
        #Mostrar expresion
        Oled.mostrar_imagen(IMAGENES[expresion_seleccionada], oled1, oled2)

        #Movimiento servomotores
        Servomotores.realizarRutinaP1(CONTROL_SERVOS, rutina_seleccionada)
        mov_activado = True
        
        #Estblecimiento del tiempo en que se activa el movimiento
        tiempo_inicial = time.time()

        return tiempo_inicial, rutina_seleccionada, mov_activado, expresion_seleccionada, comandos_realizados


    #Activación manual del movimiento y expresion
    if not automatico and mov_activado == False and comandos_realizados == False:

        #Establecimiento manual de la rutina y expresión
        rutina_seleccionada = rutina_aux
        expresion_seleccionada = expresion_aux

        #Mostrar expresion
        Oled.mostrar_imagen(IMAGENES[expresion_seleccionada], oled1, oled2)

        #Movimiento servomotores
        Servomotores.realizarRutinaP1(CONTROL_SERVOS, rutina_seleccionada)
        mov_activado = True

        #Estblecimiento del tiempo en que se activa el movimiento
        tiempo_inicial = time.time()

        return tiempo_inicial, rutina_seleccionada, mov_activado, expresion_seleccionada, comandos_realizados
    

    #Desactivación del movimiento
    if tiempo_actual - tiempo_inicial > 30 and mov_activado == True:
        Servomotores.realizarRutinaP2(CONTROL_SERVOS, rutina_seleccionada)
        mov_activado = False

        #Establece que el comando se realizó con exito
        comandos_realizados = 1

        #Establecimiento del tiempo en que se desactivo el movimiento
        tiempo_inicial = time.time()

        return tiempo_inicial, rutina_seleccionada, mov_activado, expresion_seleccionada, comandos_realizados

    
    return tiempo_inicial, rutina_aux, mov_activado, expresion_aux, comandos_realizados
    

#Entry point
if __name__ == "__main__":
    print("Es un modulo")