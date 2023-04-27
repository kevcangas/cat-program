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
                     oled1,
                     oled2,
                     automatico = True
                     ):

    if tiempo_actual - tiempo_inicial > 120 and automatico:
        rutina_seleccionada = random.choice(rutinas)
        expresion = random.choice(IMAGENES)
        Oled.mostrar_imagen(expresion, oled1, oled2)

    if rutina_seleccionada != rutina_aux and mov_activado == False:
        Servomotores.realizarRutinaP1(CONTROL_SERVOS, rutina_seleccionada)
        rutina_aux = rutina_seleccionada
        mov_activado = True
        return tiempo_inicial, rutina_aux, mov_activado

    if tiempo_actual - tiempo_inicial > 30 and mov_activado == True:
        Servomotores.realizarRutinaP2(CONTROL_SERVOS, rutina_seleccionada)
        mov_activado = False
        tiempo_inicial = time.time()
        return tiempo_inicial, rutina_aux, mov_activado
    
    return tiempo_inicial, rutina_aux, mov_activado
    

#Entry point
if __name__ == "__main__":
    print("Es un modulo")