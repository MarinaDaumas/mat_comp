import simpleplot #biblioteca usada pelo thiago motta
import math

m = 0.1 
l = 1.0 #comprimento do pendulo
g = 9.81 

D = 0.982

t = 300.0
dt = 0.01

#condições iniciais
teta_i = 0.3
omega_i = 0.

def errro(teta):
    return 0 - teta


def derivada(teta, omega):
    teta_linha = omega
    omega_linha = D*errro(teta)/(m*l**2) + g/l*teta
    return teta_linha, omega_linha


def controle_der(teta, omega):
    data = {}
    
    for i in range(int(t/dt)):
        data[round(i*dt,1)] = teta
        
        teta_linha, omega_linha = derivada(teta, omega)

        teta += teta_linha*dt
        omega += omega_linha*dt
        
    return data      
    
    
data = controle_der(teta_i, omega_i)
 
simpleplot.plot_lines('Sample', 400, 300, 'x', 'y', [data])
