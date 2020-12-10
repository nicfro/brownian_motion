from config import settings
from random import randint, uniform
import numpy as np
import math
from collections import deque  


# TODO 
# 1)
# Fix collision detection with delaunay triangulation
#
# 2) 
# Create color scheme based on particle density
# Implement color here & in main
#
# 3) 
# Handle repeated collisions, perhaps a queue could work


class Particle:
    def __init__(self, identifier, radius = 1, velocity = None, density = 2):
        self.identifier = identifier
        self.radius = radius
        self.density = density
        self.weight = self.radius**2 * self.density
        self.position = np.array([uniform(0 + self.radius, settings["x_boundary"] - self.radius), uniform(0 + self.radius, settings["y_boundary"] - self.radius)])
        self.rotation = np.array([np.cos(uniform(0, math.pi*2)), np.sin(uniform(0, math.pi*2))])
        
        self.last_collision = -99
        self.collision_deque = deque([-99, -99, -99], 5)

        self.update_properties()
        if velocity:
            self.velocity = np.array(velocity)
        else:
            self.velocity = np.array(uniform(settings["velocity_min"], settings["velocity_max"]) * self.rotation)

    @property
    def x(self):
        return self.position[0]

    @x.setter
    def x(self, value):
        self.position[0] = value

    @property
    def y(self):
        return self.position[1]

    @y.setter
    def y(self, value):
        self.position[1] = value

    @property
    def velocity_x(self):
        return self.velocity[0]

    @velocity_x.setter
    def velocity_x(self, value):
        self.velocity[0] = value

    @property
    def velocity_y(self):
        return self.velocity[1]

    @velocity_y.setter
    def velocity_y(self, value):
        self.velocity[1] = value

    def __repr__(self):
        return f"Particle with velocity {self.velocity}, position {self.position}, rotation {self.rotation} and speed {self.speed}"
    
    def update_properties(self):
        self.right = self.x + self.radius
        self.left = self.x - self.radius
        self.top = self.y - self.radius
        self.bottom = self.y + self.radius
        self.collision_box_x = self.x - (self.x % (settings["big_particle_radius"] * 2))
        self.collision_box_y = self.y - (self.y % (settings["big_particle_radius"] * 2))
        if self.last_collision != -99:
            self.collision_deque.append(self.last_collision)
        else:
            self.collision_deque.append(-99)

    def update_position(self):
        # check if particle is colliding with right or left wall
        if self.right >= settings["x_boundary"] or self.left <= 0:
            self.velocity_x = -self.velocity_x

        # check if particle is colliding with top or bottom wall
        if self.bottom >= settings["y_boundary"] or self.top <= 0:
            self.velocity_y = -self.velocity_y


        self.position += self.velocity
        self.update_properties()

    def overlaps(self, other_particle):
        return np.hypot(*(self.position - other_particle.position)) < self.radius + other_particle.radius

        
        

        
    

#particle1 = Particle()
