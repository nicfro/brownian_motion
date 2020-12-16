from config import settings
from random import randint, uniform
import numpy as np
import math
from collections import deque  


# TODO 
# 1) Make a particle spawner
#   * Make sure particle dont spawn on top of each other
#
# 2) Bind color as an attribute to the particle
#
#
class Particle:
    def __init__(self, identifier, radius = 1, velocity = None, density = 2):
        self.identifier = identifier
        self.radius = radius
        self.density = density
        #color = Color_helper(GREEN, RED, max_weight, min_weight)
        self.color = (255, 0, 0)
        self.weight = (self.radius**2) * self.density
        self.position = np.array([uniform(0 + self.radius, settings["x_boundary"] - self.radius), uniform(0 + self.radius, settings["y_boundary"] - self.radius)])
        self.rotation = np.array([np.cos(uniform(0, math.pi*2)), np.sin(uniform(0, math.pi*2))])
        
        self.last_collision = -99
        self.recent_collision = False
        self.collision_deque = deque([], 5)

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
        return f"Particle with velocity {self.velocity}, position {self.position}, rotation {self.rotation}"
    
    def update_position(self):
        # Check if particle is colliding with right or left wall
        if (self.x + self.radius >= settings["x_boundary"]) or (self.x - self.radius <= 0):
            self.velocity_x = -self.velocity_x

        # Check if particle is colliding with top or bottom wall
        if (self.y + self.radius >= settings["y_boundary"]) or (self.y - self.radius <= 0):
            self.velocity_y = -self.velocity_y

        # Update particle position
        self.position += self.velocity

        # Handle collision queue such that particles do not double collide
        if self.recent_collision:
            self.collision_deque.append(self.last_collision)
        else:
            self.collision_deque.append(-99)
        self.recent_collision = False

    def overlaps(self, other_particle):
        return np.hypot(*(self.position - other_particle.position)) < self.radius + other_particle.radius