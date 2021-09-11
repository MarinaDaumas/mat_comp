import numpy as np


class Magnet():
    def __init__(self, x, y, force):
       self.x = x
       self.y = y

       self.force = force 

    
    def force_on_pendulum(self, pendulo_pos):

        dist = [self.x - pendulo_pos[0], self.y - pendulo_pos[1]]

        mod_dist = np.sqrt(dist[0]**2+dist[1]**2)
  
        F = self.force/mod_dist**2

        F_direction = np.array([i*F/mod_dist for i in dist])
        
        return F_direction


