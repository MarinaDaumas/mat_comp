from matplotlib.pyplot import axis
import numpy as np
from numpy.core.fromnumeric import shape
import params

class Magnet():
    def __init__(self, x, y, force):
        self.x = float(x)
        self.y =  float(y)
        self.z =  params.magnets_z
        self.force = float(force) 

        
    def force_on_pendulum_one_iter(self, pendulo_pos):

        dist = [self.x - pendulo_pos[0], self.y - pendulo_pos[1]]

        mod_dist = np.sqrt(dist[0]**2+dist[1]**2+self.z**2)
  
        F = self.force/mod_dist**2

        F_direction = np.array([i/mod_dist*F for i in dist]) # vetor unitário x força
        
        print(dist, mod_dist, F_direction)

        return F_direction


    def optimized_force_on_pendulum(self, pendulo_pos):
      
        dist = -pendulo_pos + [self.x, self.y]
      
        mod_xy =  (dist**2).sum(axis=-1)  
        
        mod_dis = np.sqrt(mod_xy + self.z**2)

        unitario = dist.T/mod_dis**2

        F = self.force * (unitario/mod_dis).T  

        return F