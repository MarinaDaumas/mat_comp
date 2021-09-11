import numpy as np 
import math
import matplotlib.pyplot as plt
import params 
from utils import Magnet

still_moving = True


def beeman_position(initial_pos, l_mags):
    list_x = []
    list_y = []
    # variáveis de ambiente
    m = params.m
    L = params.L
    g = params.g
    atrito = params.atrito
    dt = params.dt
    max_iteration = params.max_iter

    # iniciando EDO
    pos = initial_pos
    vel = np.zeros(2)
    acc = np.zeros(2)

    last_vel, last_acc = vel*0, acc*0
    
    i = 0
    while i < max_iteration and still_moving:   

        # Metodo de Beeman para calclar posição
        pos += vel*dt + (2/3*acc - 1/6*last_acc)*dt**2

        next_acc = np.zeros(2)

        
        # forças agindo sobre o ima
        total_force = np.array([-m*g*pos[0]/L, -m*g*pos[1]/L]) #tensão (aproximaçaõ pela Lei de Hooke
        
        for magnet in l_mags:
            total_force += magnet.force_on_pendulum(pos) 
        
        total_force -= vel*atrito # atrito do ar
        
        next_acc += total_force/m 

        # Método segunda ordem de Adams–Moulton
        vel += (1./12)*(5*last_acc + 8*acc - last_acc)*dt
        print(pos, vel, next_acc)
        last_acc[0] = acc[0]
        acc[0] = next_acc[0]
        last_acc[1] = acc[1]
        acc[1] = next_acc[1]

        list_x.append(pos[0])
        list_y.append(pos[1])


        i+=1
    
    plt.scatter(list_x, list_y)
    plt.show()


if __name__ == "__main__":

    l_mags = [Magnet(0, 1, 1), Magnet(math.sqrt(2)/2, math.sqrt(2)/2, 1), Magnet(math.sqrt(2)/2, -math.sqrt(2)/2, 1)]

    beeman_position([3, 4], l_mags)