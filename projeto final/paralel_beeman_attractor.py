"""
Paralel processing version of beeman_attractor.py
"""
import numpy as np 
import math
import matplotlib.pyplot as plt
import params 
from utils import Magnet


batch = params.image_dim**2 # batch = num de pixels na imagem 

def calculate_acc(l_mags, pos, vel):
    # variáveis de ambiente
    m = params.m
    L = params.L
    g = params.g
    atrito = params.atrito

    next_acc = np.zeros(2)
    
    total_force = np.array([-m*g*pos[0]/L, -m*g*pos[1]/L]) # tensão (aproximaçaõ pela Lei de Hooke)
        
    for magnet in l_mags:
        total_force += magnet.force_on_pendulum(pos) 
    
    total_force -= vel*atrito # atrito do ar
    next_acc += total_force/m 

    return next_acc


def beeman_position(initial_pos, l_mags):
    list_x = []
    list_y = []

    # variáveis de ambiente
    dt = params.dt
    max_iteration = params.max_iter

    # iniciando EDO
    pos = initial_pos
    vel = np.zeros(len(initial_pos))
    acc = np.zeros(len(initial_pos))
    last_acc = acc*0

    # primeira iteração
    vel += acc*dt
    pos += vel*dt
    acc = calculate_acc(l_mags, pos, vel)
    
    i = 0
    while i < max_iteration:   

        # Metodo de Beeman para prever posição
        pos += vel*dt + (2/3*acc - 1/6*last_acc)*dt**2

        # Método de Beeman para prever velocidade    
        vel += (2/3*acc - 1/2*last_acc)*dt

        next_acc = calculate_acc(l_mags, pos, vel ) 

        # Método para corrigir velocidade
        vel += (1./12)*(5*next_acc + 8*acc - last_acc)*dt
        print(i, pos, vel, next_acc)

        last_acc[0] = acc[0]
        acc[0] = next_acc[0]
        last_acc[1] = acc[1]
        acc[1] = next_acc[1]

        list_x.append(pos[0])
        list_y.append(pos[1])

        i+=1
    
    plt.scatter(list_x, list_y)
    plt.scatter([1,-math.sqrt(2), -math.sqrt(2) ], [0,-math.sqrt(2), math.sqrt(2)])
    plt.show()


if __name__ == "__main__":

    l_mags = [Magnet(1, 0, -0.5, 2), Magnet(-math.sqrt(2), math.sqrt(2), -0.5, 2), Magnet(-math.sqrt(2), -math.sqrt(2), -0.5, 2)]

    beeman_position([-0., 2.015], l_mags)