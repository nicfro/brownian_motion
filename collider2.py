from itertools import combinations
import numpy as np


class Collide:
    def __init__(self, particles):
        self.particles = particles
        self.handle_collisions()
    
    def change_velocities(self, p1, p2):
        m1, m2 = p1.density * p1.radius**2, p2.density * p2.radius**2
        M = m1 + m2
        r1, r2 = p1.position, p2.position
        d = np.linalg.norm(r1 - r2)**2
        v1, v2 = p1.velocity, p2.velocity
        u1 = v1 - 2*m2 / M * np.dot(v1-v2, r1-r2) / d * (r1 - r2)
        u2 = v2 - 2*m1 / M * np.dot(v2-v1, r2-r1) / d * (r2 - r1)
        p1.velocity = u1
        p2.velocity = u2

    def handle_collisions(self):
        pairs = combinations(range(len(self.particles)), 2)
        for i,j in pairs:
            if self.particles[i].overlaps(self.particles[j]):
                self.change_velocities(self.particles[i], self.particles[j])