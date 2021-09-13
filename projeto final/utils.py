import numpy as np
from numpy.core.fromnumeric import shape


class Magnet():
    def __init__(self, x, y, z, force, number):
        self.x = float(x)
        self.y =  float(y)
        self.z =  float(z)
        self.force = float(force) 
        self.number = int(number)

    
    def force_on_pendulum(self, pendulo_pos):

        dist = -pendulo_pos + [self.x, self.y]

        mod_dist = [np.sqrt(i[0]**2+i[1]**2+self.z**2) for i in dist]
  
        F = np.ones(len(mod_dist))

        F = [F[i]*self.force/mod_dist[i]**2 for i in range(len(F))]

        F_direction = np.array([dist[i]*F[i]/mod_dist[i] for i in range(len(dist))]) # vetor unitário x força
        
        return F_direction


    def distance(self, pendulo_pos):

        dist = -pendulo_pos + [self.x, self.y]
        
        mod_dist = [np.sqrt(i[0]**2+i[1]**2+self.z**2) for i in dist]

        return mod_dist

        
    
    def force_on_pendulum_one_iter(self, pendulo_pos):

        dist = [self.x - pendulo_pos[0], self.y - pendulo_pos[1]]

        mod_dist = np.sqrt(dist[0]**2+dist[1]**2+self.z**2)
  
        F = self.force/mod_dist**2

        F_direction = np.array([i/mod_dist*F for i in dist]) # vetor unitário x força
        
        return F_direction

