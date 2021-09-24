import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from beeman_attractor import beeman_position 
from utils import Magnet



def set_magnets():
    """
    Initialises magnets positions and forces.
    """
    n = int(input("Numero de imas: "))
    list_mags = []

    print("Todos os imas devem ter coordenadas (x,y) tais que -3 < x e y < -3.\nForças positivas são atrativas e negativas repulsivas.")

    for i in range(n):
        x = input("x ima "+ str(i) +': ')
        y = input("x ima "+ str(i) +': ')
        z = input("z ima "+ str(i) +': ')
        force = input("força ima "+ str(i) +': ')
        list_mags.append(Magnet(x, y, z, force, i))

    return list_mags    

def main():

    t_0 = datetime.now()

    #list_mags = set_magnets()
    list_mags = [Magnet(2, -2, 10, 0), Magnet(-2, -1, 10, 1), Magnet(2, 2, 10, 2)]

    initial_pos = []
    for i in range(-30, 30):
        for j in range(-30, 30):
            initial_pos.append([i, j])
    
    initial_pos_1 = [3., 3.]

    im = beeman_position(initial_pos_1, list_mags)

    print(im, initial_pos_1)
    t_1 = datetime.now()

    print(t_1 - t_0)

    # plt.scatter(list_x, list_y)
    # plt.scatter([1,-math.sqrt(2), -math.sqrt(2) ], [0,-math.sqrt(2), math.sqrt(2)])
    # plt.show()

if __name__ == "__main__":
    main()

