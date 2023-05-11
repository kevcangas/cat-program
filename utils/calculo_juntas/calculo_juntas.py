from math import *
import numpy as np


#Calculo juntas de las patas traseras
def calculo_juntas_PT(L1,
                      L2,
                      L3,
                      Z0,
                      xC, 
                      yC,
                      z, 
                      POSICION_SERVO_HOMBRO, 
                      Q0_INICIAL, 
                      Q0_MIN, 
                      Q0_MAX,
                      Q1_INICIAL, 
                      Q1_MIN, 
                      Q1_MAX,
                      Q2_INICIAL, 
                      Q2_MIN, 
                      Q2_MAX,
                      ):
    #Puntos a evaluar 
    x=xC
    y=yC
    z=z

    #Punto en el marco original
    p0 = [x,y,z] 
    
    #Calculo de las variables de juntas
    alpha = acos(z/sqrt(z**2+y**2))
    phi = atan2(y,z)
    q0=POSICION_SERVO_HOMBRO
    
    if alpha>abs(phi):
        q0=phi+alpha
    else:
        q0=phi+alpha
    
    #Rotación del plano
    R = np.array([[1, 0, 0],
        [0, cos(-q0), -sin(-q0)],
        [0, sin(-q0), cos(-q0)]])
    
    d = np.transpose(np.array([0, Z0*sin(q0), Z0*cos(q0)]))
    
    p1 = np.linalg.inv(R)*(p0-d)
    
    #Calculo de q1,q2 y q3
    xc = p1[0][0]
    yc = p1[1][1]
    
    a = (L3*L2)/(L1+L3)
    b = (L3*sqrt(xc**2+yc**2))/(L1+L3)

    beta = acos((b**2+L3**2-a**2)/(2*b*L3))
    theta = atan2(yc,xc)
    
    if beta>abs(theta):
        q1 = beta+theta
    else:
        q1 = theta+beta
    
    #Resumen variables
    q0 = q0.real + Q0_INICIAL
    q1 = pi + q1.real - Q1_INICIAL
    q2 = acos((a**2+L3**2-b**2)/(2*a*L3)).real + Q2_INICIAL
    q3 = q2

    #Ajuste de las variables con valores MAX y MIN
    if q0 > Q0_MAX:
        q0 = Q0_MAX
        print("PT Se alcanzó el tope max en q0")
    elif q0 < Q0_MIN:
        q0 = Q0_MIN
        print("PT Se alcanzó el tope min en q0")
    
    if q1 > Q1_MAX:
        q1 = Q1_MAX
        print("PT Se alcanzó el tope max en q1")
    elif q1 < Q1_MIN:
        q1 = Q1_MIN
        print("PT Se alcanzó el tope min en q1")
    
    if q2 > Q2_MAX:
        q2 = Q2_MAX
        print(f"PT Se alcanzó el tope max en q2 {q2}")
    elif q2 < Q2_MIN:
        q2 = Q2_MIN
        print(f"PT Se alcanzó el tope min en q2 {q2}")

    #Agregado de las variables al vector a guardar
    return round(q0*180/pi), round(q1*180/pi), round(q2*180/pi)


#Calculo juntas de las patas traseras
def calculo_juntas_PD(L1,
                      L2,
                      Z0,
                      Z1,
                      xC, 
                      yC,
                      z, 
                      POSICION_SERVO_HOMBRO, 
                      Q0_INICIAL, 
                      Q0_MIN, 
                      Q0_MAX,
                      Q1_INICIAL, 
                      Q1_MIN, 
                      Q1_MAX,
                      Q2_INICIAL, 
                      Q2_MIN, 
                      Q2_MAX,
                      ):
    
    x=xC
    y=yC
    z=z

    #Punto en el marco original
    p0 = [x,y,z]
            
    #Calculo de las variables de juntas
    alpha = acos((Z0-Z1)/sqrt(z**2+y**2))
    phi = atan2(y,z)
    q0=POSICION_SERVO_HOMBRO
    
    if alpha>abs(phi):
        q0=phi+alpha
    else:
        q0=phi+alpha
    
    #Rotación del plano
    R = np.array([[1, 0, 0],
        [0, cos(-q0), -sin(-q0)],
        [0, sin(-q0), cos(-q0)]])
    
    d = np.transpose(np.array([0, (Z0-Z1)*sin(q0), (Z0-Z1)*cos(q0)]))
     
    #Punto en el plano rotado
    p1 = np.linalg.inv(R)*(p0-d) 
    
    #Calculo de q1,q2
    xc = p1[0][0]
    yc = p1[1][1]
    
    q2 = acos((L1**2+L2**2-(xc**2+yc**2))/(2*L1*L2))
    
    beta = acos(((xc**2+yc**2)+L1**2-L2**2)/(2*sqrt(xc**2+yc**2)*L1))
    theta = atan(yc/xc)

    if xc<0:
        theta=theta-pi
    
    q1 = - beta + theta

    #print(q1)
    #Resumen variables
    q0 = q0.real + Q0_INICIAL
    q1 = q1.real + pi - Q1_INICIAL 
    q2 = q2.real + Q2_INICIAL

    #Ajuste de las variables con valores MAX y MIN
    if q0 > Q0_MAX:
        print(f"PD Se alcanzó el tope max en q0 {q0}")
        q0 = Q0_MAX
    elif q0 < Q0_MIN:
        print(f"PD Se alcanzó el tope min en q0 {q0}")
        q0 = Q0_MIN
        
    if q1 > Q1_MAX:
        print(f"PD Se alcanzó el tope max en q1 {q1}")
        q1 = Q1_MAX
    elif q1 < Q1_MIN:
        print(f"PD Se alcanzó el tope min en q1 {q1}")
        q1 = Q1_MIN
        
    
    if q2 > Q2_MAX:
        q2 = Q2_MAX
        print("PD Se alcanzó el tope max en q2")
    elif q2 < Q2_MIN:
        q2 = Q2_MIN
        print("PD Se alcanzó el tope min en q2")

    #Agregado de las variables al vector a guardar
    return round(q0*180/pi), round(q1*180/pi), round(q2*180/pi)