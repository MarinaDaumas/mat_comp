"""
Paralel processing version of beeman_attractor.py
"""
import numpy as np 
import math
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import partition
import params 
from utils import Magnet


batch = params.image_dim**2 # batch = num de pixels na imagem 

def calculate_acc(l_mags, pos, vel):
    # variáveis de ambiente
    m = params.m
    L = params.L
    g = params.g
    atrito = params.atrito

    total_force = -m*g/L*pos #tensão (aproximaçaõ pela Lei de Hooke)
        
    for magnet in l_mags:
        total_force += magnet.force_on_pendulum(pos) 
    
    total_force -= vel*atrito # atrito do ar

    next_acc = total_force/m 

    return next_acc


def final_magnet(final_pos, l_mags, initial_pos):

    dist = []

    for magnet in l_mags:
        dist.append(magnet.distance(final_pos))

   
    return np.argmin(dist, 0)


def beeman_position(initial_pos, l_mags):
    list_x = []
    list_y = []

    # variáveis de ambiente
    dt = params.dt
    max_iteration = params.max_iter

    # iniciando EDO
    pos = initial_pos
    vel = np.zeros(np.shape(initial_pos))
    acc = np.zeros(np.shape(initial_pos))
    last_acc = acc*0
    

    # primeira iteração
    vel += acc*dt
    pos += vel*dt
    acc = calculate_acc(l_mags, pos, vel)
    print(pos[2], vel[2], acc[2])
    i = 0
    while i < max_iteration:   

        # Metodo de Beeman para prever posição
        pos += vel*dt + (2/3*acc - 1/6*last_acc)*dt**2

        # Método de Beeman para prever velocidade    
        vel += (2/3*acc - 1/2*last_acc)*dt

        next_acc = calculate_acc(l_mags, pos, vel) 
        print(pos[2], vel[2], next_acc[2])
        # Método para corrigir velocidade
        vel += (1./12)*(5*next_acc + 8*acc - last_acc)*dt
        print(vel[2])

        # update EDO variables
        last_acc = acc.copy()
        acc = next_acc.copy()
      
        
        list_x.append(pos[2][0])
        list_y.append(pos[2][1])
        
        i+=1
    
    plt.scatter(list_x, list_y)
    plt.scatter([1,-math.sqrt(2), -math.sqrt(2) ], [0,-math.sqrt(2), math.sqrt(2)])
    plt.show()

    final_color = final_magnet(pos, l_mags, initial_pos)

    return final_color

if __name__ == "__main__":
    pass