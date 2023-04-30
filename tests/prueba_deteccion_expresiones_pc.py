#PRUEBA: PRUEBA DE LA LIBRERÍA DETECCIONEXPRESIONES

#Librerías externas
import cv2

#Librerías locales
import functions.DeteccionExpresiones as DE


#Inicialización
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
detector_rostros = DE.cargar_Cascade()
red_convolucional = DE.cargar_CNN()


#Programa principal
try:
    while(1):
        DE.deteccion_expresiones(cap,
                                 detector_rostros, 
                                 red_convolucional, 
                                 verbose=True, 
                                 mostrar_ima=True)


except ValueError as ve:
    print(ve)


except KeyboardInterrupt:
    print('Programa detenido')