import tflite_runtime.interpreter as tflite
import cv2
import numpy as np
from numpy import float32


#Carga de la red neuronal convolucional entrenada
#retorna el objeto ya instanciado
def cargar_CNN():
    model=tflite.Interpreter(model_path=r'./data/redneuronal/model.tflite')
    model.allocate_tensors()
    return model


#Carga del clasificador Cascade para detección de rostros
def cargar_Cascade():
    face_cascade_name = r'./data/redneuronal/haarcascade_frontalface_alt.xml'
    face_cascade = cv2.CascadeClassifier()
    if not face_cascade.load(face_cascade_name):
        print('Error al cargar Face Cascade')
        exit(0)
    return face_cascade


#Esta función retorna una imagen que contiene el rostro captado por la
#cámara
def detectar_rostro(frame,face_cascade):
    faces = face_cascade.detectMultiScale(frame)
    if len(faces)!=0:
        (x,y,w,h)=faces[0]
        return frame[y:y+h,x:x+w]
    else:
        return frame
    

#Función para la detección de las expresiones, retorna una etiqueta con el 
#valor de la expresión detectada
def deteccion_expresiones(cap, detector_rostros, red_convolucional, verbose:bool = False, mostrar_ima:bool = False):
    #Procesamiento de la imagen
    ret, frame = cap.read() #Obtención de la imagen de la cámara
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Conversión a escala de grises
    frame = detectar_rostro(frame, detector_rostros) #Detección del rostro
    frame_a_mostrar = frame
    frame = cv2.resize(frame, (48,48), interpolation = cv2.INTER_CUBIC) #Rescalamiento a 48x48 pixeles

    #Conversión de las imagenes de matriz a vector
    x_test = np.array(frame)
    x_test = np.expand_dims(x_test,axis=0)
    x_test = np.expand_dims(x_test,axis=-1)
    red_convolucional.set_tensor(0, x_test.astype(float32))
    red_convolucional.invoke()
    prediccion = np.argmax(red_convolucional.get_tensor(32)[0])

    #Clasificación
    #etiqueta = ''

    if prediccion == 0:  
        etiqueta='Enojo'

    if prediccion == 1:  
        etiqueta='Alegria'

    if prediccion == 2: 
        etiqueta='Neutro'

    if prediccion == 3: 
        etiqueta='Tristeza'

    if verbose: print(etiqueta)
    
    if mostrar_ima: cv2.imshow('imagen',frame_a_mostrar)
    
    if cv2.waitKey(1) == ord('q'):
        raise ValueError("Programa Detenido")

    return prediccion


#Entry point
if __name__ == '__main__':
    print('This is a module')