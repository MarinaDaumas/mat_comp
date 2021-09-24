import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import params
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
        force = input("força ima "+ str(i) +': ')
        list_mags.append(Magnet(x, y, force, i))

    return list_mags    

def main():

    
    x = []
    y = [] 
    #list_mags = set_magnets()
    list_mags = [Magnet(2, -2, 10, 0), Magnet(-2, -2, 10, 2)]

    t_0 = datetime.now()
    size  = params.image_dim

    divisor = size/10 

    initial_pos = []
    for i in range(-int(size/2), int(size/2)):
        for j in range(-int(size/2), int(size/2)):
            initial_pos.append([float(i/divisor), float(j/divisor)])
 

    im = beeman_position(initial_pos, list_mags)
    k = 0
    result = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            result[i][j] = im[k]
            k+=1

    plt.pcolormesh(result)
    
    t_1 = datetime.now()
    print(t_1 - t_0)

    plt.show()
       


if __name__ == "__main__":
    main()

