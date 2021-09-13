import numpy as np


class Magnet():
    def __init__(self, x, y, z, force):
        self.x = x
        self.y = y
        self.z = z
        self.force = force 

    
    def force_on_pendulum(self, pendulo_pos):

        dist = [self.x - pendulo_pos[0], self.y - pendulo_pos[1]]

        mod_dist = np.sqrt(dist[0]**2+dist[1]**2+self.z**2)
  
        F = self.force/mod_dist**2

        F_direction = np.array([i/mod_dist*F for i in dist]) # vetor unitário x força
        
        return F_direction


