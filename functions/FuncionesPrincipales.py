#Python
import time
import random


#Propias
from functions import Servomotores


#Esta función realiza el movimiento de las extremidades
def rutinaControlada(tiempo_actual, tiempo_inicial, CONTROL_SERVOS, rutinas):
    if tiempo_actual - tiempo_inicial > 120:
        rutina_seleccionada = random.choice(rutinas)

        if rutina_seleccionada != rutina_aux and mov_activado:
            Servomotores.realizarRutinaP1(CONTROL_SERVOS, rutina_seleccionada)
            rutina_aux = rutina_seleccionada
            mov_activado = True

        if tiempo_actual - tiempo_inicial > 30:
            Servomotores.realizarRutinaP2(CONTROL_SERVOS, rutina_seleccionada)

        return time.time()
    
    else:
        return tiempo_inicial
    

#Entry point
if __name__ == "__main__":
    print("Es un modulo")