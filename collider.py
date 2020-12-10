# https://scipython.com/blog/two-dimensional-collisions/
from collections import defaultdict
import numpy as np
from itertools import combinations
from config import settings

class Collide:
    def __init__(self, particles):
        self.collision_cells = defaultdict(lambda: defaultdict(list))
        self.cell_size = settings["big_particle_radius"] * 2
        self.particles = particles
        self.populate_collision_cells()
        self.handle_collisions()

    def populate_collision_cells(self):
        for particle in self.particles:
            self.collision_cells[particle.collision_box_x][particle.collision_box_y].append(particle)

    def handle_collisions(self):
        for i in self.collision_cells:
            for j in self.collision_cells[i]:
                if len(self.collision_cells[i][j]) > 1:
                    pairs = combinations(self.collision_cells[i][j], 2)
                    for x,y in pairs:
                        if x.overlaps(y):
                            if (x.identifier != y.last_collision) or (y.identifier != x.last_collision):
                                self.change_velocities(x, y)
                                y.last_collision = x.identifier
                                x.last_collision = y.identifier


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
