#PRUEBA: ACTIVACIÓN CAMARA

import cv2  
import time

cap = cv2.VideoCapture(0)
#time.sleep(5)

while True:
    ret, frame = cap.read()
    print(f'{frame.shape}')
    if cv2.waitKey(1) == ord('q'):
        break
