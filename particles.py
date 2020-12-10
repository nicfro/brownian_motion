from config import settings
from random import randint, uniform
import numpy as np
import math


class Particle:
    def __init__(self, identifier, radius = 1, velocity = None, density = 2):
        self.identifier = identifier
        self.radius = radius
        self.density = density
        #self.color = self.density * RGB GRADIENT
        self.position = np.array([randint(0 + self.radius, settings["x_boundary"] - self.radius), randint(0 + self.radius, settings["y_boundary"] - self.radius)]).astype(np.float32)
        self.update_properties()

        self.rotation = np.array([np.cos(uniform(0, math.pi*2)), np.sin(uniform(0, math.pi*2))])
        if velocity:
            self.velocity = np.array(velocity)
        else:
            self.velocity = np.array(uniform(settings["velocity_min"], settings["velocity_max"]) * self.rotation)
        self.speed = np.linalg.norm(self.velocity)
        self.last_collision = -99

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

    def __repr__(self):
        return f"Particle with velocity {self.velocity}, position {self.position}, rotation {self.rotation} and speed {self.speed}"
    
    def update_properties(self):
        self.right = self.position[0] + self.radius
        self.left = self.position[0] - self.radius
        self.top = self.position[1] - self.radius
        self.bottom = self.position[1] + self.radius
        self.collision_box_x = self.position[0] - (self.position[0] % (settings["big_particle_radius"] * 2))
        self.collision_box_y = self.position[1] - (self.position[1] % (settings["big_particle_radius"] * 2))
        #self.last_collision = -99

    def update_position(self):
        # check if particle is colliding with right or left wall
        if self.right >= settings["x_boundary"] or self.left <= 0:
            self.velocity = np.array([-self.velocity[0], self.velocity[1]])

        # check if particle is colliding with top or bottom wall
        if self.bottom >= settings["y_boundary"] or self.top <= 0:
            self.velocity = np.array([self.velocity[0], -self.velocity[1]])

        self.position += self.velocity
        self.update_properties()

    def overlaps(self, other_particle):
        return np.hypot(*(self.position - other_particle.position)) < self.radius + other_particle.radius

        
        

        
    

#particle1 = Particle()
