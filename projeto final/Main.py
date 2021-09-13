import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from paralel_beeman_attractor import beeman_position 
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
    list_mags = [Magnet(2, 1, 1, 1, 1), Magnet(-3, -3, 1, 1, 2)]
    initial_pos = []
    for i in range(-30, 30):
        for j in range(-30, 30):
            initial_pos.append([i, j])
    
    initial_pos_1 = [[1., 1.],[-4., 2], [0.5, -2]]

    im = beeman_position(initial_pos_1, list_mags)

    print(im, initial_pos_1)
    t_1 = datetime.now()

    print(t_1 - t_0)

if __name__ == "__main__":
    main()

