#PRUEBA: PRUEBA DE LA LIBRERÍA DETECCIONEXPRESIONES

#Librerías externas
import cv2

#Librerías locales
import functions.DeteccionExpresionesRasp as DE


#Programa principal
def run():

    #Inicialización
    cap = cv2.VideoCapture(0)
    detector_rostros = DE.cargar_Cascade()
    red_convolucional = DE.cargar_CNN()

    try:
        while(1):
            DE.deteccion_expresiones(cap,
                                    detector_rostros, 
                                    red_convolucional, 
                                    verbose=True, 
                                    mostrar_ima=False)


    except ValueError as ve:
        print(ve)


    except KeyboardInterrupt:
        print('Programa detenido')


if __name__ == '__main__':
    run()