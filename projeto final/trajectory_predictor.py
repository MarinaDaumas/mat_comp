import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from beeman_attractor import beeman_position 
from utils import Magnet

"""
Esse programa tem o objetivo de calcular e apresentar o movimento 
caótico determinístico do sistema de pêndulo magnético para 3 posições 
inicias escolhidas pelo usuário.
O número de ímãs do sistema assim como suas respectivas posições e forças 
exercidas no pêndulo são determinas pelo usuário.
Outras váriáveis podem ser modificados diretamente no arquivo params.py.
"""

def initial_settings():
    """
    Inicia as posições e forças magnéticas para cada ímã e as posições iniciais do pêndulo.  
    """
    n = int(input("Numero de imas: "))
    list_mags = []
    in_x = []
    in_y = []

    print("Pelo menos um dos ímãs deve ser atrativo e todos devem ter coordenadas (x,y) tais que -3 < x e y < -3.\nForças positivas são atrativas e negativas repulsivas.")

    for i in range(1, n+1):
        x = input("\nx ima "+ str(i) +': ')
        y = input("y ima "+ str(i) +': ')
        force = input("força ima "+ str(i) +': ')
        list_mags.append(Magnet(x, y, force))

    for i in range(1, 4):
        print("\nEscolha a posição inicial do pêndulo " + str(i) + "." )
        in_x.append(float(input("x" + str(i) + ": ")))
        in_y.append(float(input("y" + str(i) + ": ")))

    initial_pos = {"x": in_x, "y": in_y}

    return list_mags, initial_pos    


def main():

    t_0 = datetime.now()

    list_mags, initial_pos = initial_settings()
    #list_mags = [Magnet(2, -2, 10), Magnet(-2, -1, 10), Magnet(2, 2, 10)]

    list_x = []
    list_y = []
    for i in range(3):

        x, y = beeman_position([initial_pos["x"][i],initial_pos["y"][i]], list_mags)
        list_x.append(x)
        list_y.append(y)


    t_1 = datetime.now()
    print("\nTempo de processamento: ", t_1 - t_0)

    
    # Plot movimento pêndulo
    mags_x = []
    mags_y = []
    for mag in list_mags:
        mags_x.append(mag.x)  
        mags_y.append(mag.y)

    for i in range(2):
        plt.scatter(list_x[i], list_y[i], s=1)
    plt.scatter(mags_x, mags_y, s=30)
    plt.show()


if __name__ == "__main__":
    main()

