# https://scipython.com/blog/two-dimensional-collisions/
from collections import defaultdict
import numpy as np
from itertools import combinations
from config import settings
from scipy import spatial

class Collide:
    def __init__(self, particles):
        self.collision_distance = settings["big_particle_radius"] * 1.5
        self.particles = particles
        self.tree = spatial.cKDTree(np.array([x.position for x in particles]))
        self.handle_collisions()

    def change_velocities(self, p1, p2):
        m1, m2 = p1.radius**2, p2.radius**2
        M = m1 + m2
        r1, r2 = p1.position, p2.position
        d = np.linalg.norm(r1 - r2)**2
        v1, v2 = p1.velocity, p2.velocity
        u1 = v1 - 2*m2 / M * np.dot(v1-v2, r1-r2) / d * (r1 - r2)
        u2 = v2 - 2*m1 / M * np.dot(v2-v1, r2-r1) / d * (r2 - r1)
        p1.velocity = u1
        p2.velocity = u2

    def handle_collisions(self):
        for x, y in self.tree.query_pairs(self.collision_distance):
            x = self.particles[x]
            y = self.particles[y]

            if (x.identifier not in  y.collision_deque) or (y.identifier not in x.collision_deque):
                if x.overlaps(y):
                    self.change_velocities(x, y)
                    y.last_collision = x.identifier
                    y.recent_collision = True
                    x.last_collision = y.identifier
                    x.recent_collision = True

    def get_collisions(self):
        collisions = []
        for x, y in self.tree.query_pairs(self.collision_distance):
            #x = self.particles[x]
            #y = self.particles[y]
            collisions.append([x,y])
        return collisions

