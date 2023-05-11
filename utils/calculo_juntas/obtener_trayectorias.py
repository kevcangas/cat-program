#Python
import numpy as np
import matplotlib.pyplot as plt


#Librerías propias
from utils.calculo_juntas.bezier import Bezier


def obtener_trayectoria():
    t_points = np.arange(0, 1, 0.01)
    coordenadas=[]

    cantidad_pts_itr = int(input("Ingresar la cantidad de puntos para la interpolación: "))

    for i in range(cantidad_pts_itr):
        x = int(input(f"Ingresa la abscisa del punto {i}: "))
        y = int(input(f"Ingresa la ordenada del punto {i}: "))
        print(f"Punto {i}: [{x}, {y}]")
        coordenadas.append([x,y])

    coordenadas = np.array(coordenadas)
    curve1 = Bezier.Curve(t_points, coordenadas)

    plt.plot(
        coordenadas[:, 0],
        coordenadas[:, 1],
        'y--',
        label='Puntos de generación'
    )

    plt.plot(
        coordenadas[:, 0],
        coordenadas[:, 1],
        'yo',
        label='Puntos de generación'
    )

    plt.plot(
        curve1[:, 0],   # x-coordinates.
        curve1[:, 1],    # y-coordinates.
        label = 'Trayectoria'
    )

    plt.plot(
        coordenadas[0][0],
        coordenadas[0][1],
        'ro',
        label = 'Inicio'
    )

    plt.plot(
        coordenadas[-1][0],
        coordenadas[-1][1],
        'go',
        label = 'Final'
    )

    plt.title("Trayectoria")
    plt.legend(loc = "upper left")

    plt.xlim([-180,180])
    plt.ylim([-200,0])

    plt.show()

    return curve1[:, 0], curve1[:, 1]