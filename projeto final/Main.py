import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import params
from datetime import datetime
from paralel_beeman_attractor import beeman_position 
from utils import Magnet


def set_magnets():
    """
    Initialises magnets positions and attraction forces.
    """
    n = int(input("Numero de imas: "))
    list_mags = []

    print("Pelo menos um dos ímãs deve ser atrativo e todos devem ter coordenadas (x,y) tais que -3 < x e y < -3.\nForças positivas são atrativas e negativas repulsivas.")

    for i in range(n):
        x = input("x ima "+ str(i) +': ')
        y = input("x ima "+ str(i) +': ')
        force = input("força ima "+ str(i) +': ')
        list_mags.append(Magnet(x, y, force, i))

    return list_mags    

def main(): 

    show_regions = input("Deseja ver o mapa em cores da posição final do pêndulo?\n(S - Sim  N - não)\n")
    #list_mags = set_magnets()
    list_mags = [Magnet(2, -5, 10, 0), Magnet(2, 2, 8, 1), Magnet(-3, -3, 11, 2)]

    t_0 = datetime.now()


    size  = params.image_dim
    divisor = size/10 

    initial_pos =[]
    for i in range(-int(size/2), int(size/2)):
        for j in range(-int(size/2), int(size/2)):
            initial_pos.append([float(j/divisor), float(-i/divisor)])

    initial_pos = np.array(initial_pos)
    final_pos = beeman_position(initial_pos, list_mags)

    k = 0
    result = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            result[i][j] = final_pos[k]
            k+=1
    

    
    ajust = int(255/(len(list_mags)-1))

    res_image = result.astype('uint8')*ajust #ajusta os valores de cor na escala GRAY
    contours, hierarchy = cv.findContours(res_image, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)
    res_image = cv.cvtColor(res_image, cv.COLOR_GRAY2BGR)

    black = np.zeros(np.shape(res_image)).astype('uint8')
    cv.drawContours(image=black, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=1, lineType=cv.LINE_AA)
    caos_map = cv.resize(black, [720, 720])

    t_1 = datetime.now()
    print(t_1 - t_0)

    cv.imshow("Regiões de Caos", caos_map)
    cv.waitKey(0)

    
    # plota em cores as regiões de cada ímã
    if show_regions in ['s','S']:
        
        reversed_result = result.copy()
        for i in range(len(result)):
            reversed_result[-i-1] = result[i] 

        plt.pcolormesh(reversed_result)
    
        plt.axis('off')
        plt.show()

if __name__ == "__main__":
    main()

