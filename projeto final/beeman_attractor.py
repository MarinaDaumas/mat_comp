"""
Beeman attractor para apenas um ponto inicial.
"""
from matplotlib.colors import to_rgba_array
import numpy as np 
import math
import matplotlib.pyplot as plt
import params 
from utils import Magnet


def calculate_acc(l_mags, pos, vel):
    # variáveis de ambiente
    m = params.m
    L = params.L
    g = params.g
    atrito = params.atrito

    total_force = np.array([-m*g*pos[0]/L, -m*g*pos[1]/L]) #tensão (aproximaçaõ pela Lei de Hooke)
        
    for magnet in l_mags:
        total_force += magnet.force_on_pendulum_one_iter(pos) 

    total_force -= vel*atrito # atrito do ar
    next_acc = total_force/m 

    return next_acc


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
    last_acc = np.zeros(np.shape(initial_pos))


    i = 0
    while i < max_iteration:   

        # Metodo de Beeman para prever posição
        pos += vel*dt + (2/3*acc - 1/6*last_acc)*dt**2

        # Método de Beeman para prever velocidade    
        vel += (2/3*acc - 1/2*last_acc)*dt

        # Aceleeração
        next_acc = calculate_acc(l_mags, pos, vel) 

        # Método para corrigir velocidade
        vel += (1./12)*(5*next_acc + 8*acc - last_acc)*dt


        # Update variáveis
        last_acc = acc.copy()
        acc = next_acc.copy()
       
    
        list_x.append(pos[0])
        list_y.append(pos[1])

        i+=1

    return list_x, list_y

