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
                     automatico = True
                     ):

    if tiempo_actual - tiempo_inicial > 120 and automatico:
        rutina_seleccionada = random.choice(rutinas)
        expresion_seleccionada = random.choice(imagenes_automatico)
        Oled.mostrar_imagen(IMAGENES[expresion_seleccionada], oled1, oled2)


    elif not automatico:
        rutina_seleccionada = rutina_aux
        expresion_seleccionada = expresion_aux
        Oled.mostrar_imagen(IMAGENES[expresion_seleccionada], oled1, oled2)


    if tiempo_actual - tiempo_inicial > 120 and mov_activado == False:
        Servomotores.realizarRutinaP1(CONTROL_SERVOS, rutina_seleccionada)
        mov_activado = True
        return tiempo_inicial, rutina_seleccionada, mov_activado, expresion_seleccionada


    if tiempo_actual - tiempo_inicial > 30 and mov_activado == True:
        Servomotores.realizarRutinaP2(CONTROL_SERVOS, rutina_seleccionada)
        mov_activado = False
        tiempo_inicial = time.time()
        return tiempo_inicial, rutina_seleccionada, mov_activado, expresion_seleccionada
    
    return tiempo_inicial, rutina_seleccionada, mov_activado, expresion_seleccionada
    

#Entry point
if __name__ == "__main__":
    print("Es un modulo")