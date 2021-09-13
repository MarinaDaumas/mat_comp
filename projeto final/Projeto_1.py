import cv2 as cv
import numpy as np
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
        force = input("força ima "+ str(i) +': ')
        list_mags.append(Magnet(x, y, force))

    return list_mags    

def main():
    #list_mags = set_magnets()
    total_force = np.array([.1, .8])
    vel = np.array([.2, .2])
    atrito = 1
    total_force -= vel*atrito # atrito do ar
    print(total_force)


if __name__ == "__main__":
    main()

