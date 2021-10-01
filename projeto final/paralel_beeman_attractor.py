"""
Paralel processing version of beeman_attractor.py
"""
import numpy as np 
import math
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import partition
import params 
from utils import Magnet



def get_acc(l_mags, pos, vel):
    # variáveis de ambiente
    m = params.m
    L = params.L
    g = params.g
    atrito = params.atrito

    total_force = -m*g/L*pos #tensão (aproximaçaõ pela Lei de Hooke)
        
    for magnet in l_mags:
        total_force += magnet.optimized_force_on_pendulum(pos) 
        
    total_force -= vel*atrito # atrito do ar

    next_acc = total_force/m 

    return next_acc


def final_magnet(final_pos, l_mags):
    
    dist_array =np.zeros((len(final_pos), len(l_mags)))  
    for s in range(len(l_mags)):
        dist_array[:,s] = ((final_pos - [l_mags[s].x, l_mags[s].y])**2).sum(axis=1)
    return np.argmin(dist_array,axis=1)    
   

def beeman_position(initial_pos, l_mags):
    
    # variáveis de ambiente
    dt = params.dt
    max_iteration = params.max_iter

    # iniciando EDO
    pos = initial_pos
    vel = np.zeros(np.shape(initial_pos))
    acc = np.zeros(np.shape(initial_pos))
    last_acc = np.zeros(np.shape(initial_pos))
    

    # # primeira iteração
    # vel += acc*dt
    # pos += vel*dt
    # acc = get_acc(l_mags, pos, vel)
    
    i = 0
    while i < max_iteration:   

        # Metodo de Beeman para prever posição
        pos += vel*dt + (2/3*acc - 1/6*last_acc)*dt**2

        # Método de Beeman para prever velocidade    
        vel += (2/3*acc - 1/2*last_acc)*dt

        next_acc = get_acc(l_mags, pos, vel) 

        # Método para corrigir velocidade
        vel += (1./12)*(5*next_acc + 8*acc - last_acc)*dt

        # update EDO variables
        last_acc = acc.copy()
        acc = next_acc.copy()     
        
        i+=1
    
    final_color = final_magnet(pos, l_mags)
   
    return final_color

if __name__ == "__main__":
    pass