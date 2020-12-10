import pygame
import numpy as np
import math
import particles
from config import settings
from collections import defaultdict
import collider
import collider_ball_tree
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = [settings["x_boundary"], settings["y_boundary"]]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Brownian Motion")
 
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
particles_array = []

counter = 0
for i in range(settings["number_of_particles"]):
    particle = particles.Particle(identifier = counter, radius = random.uniform(2, 20), density = random.uniform(2, 10))
    #particle = particles.Particle(identifier = counter, radius = settings["small_particle_radius"])
    particles_array.append(particle)
    counter += 1

particles_array.append(particles.Particle(identifier = counter, radius = settings["big_particle_radius"], velocity=[0,0]))

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    collider_ball_tree.Collide(particles = particles_array)

    for particle in particles_array:
        pygame.draw.circle(color=RED, surface=screen, center=particle.position, radius=particle.radius)
        particle.update_position()
    
    # --- Limit to 60 frames per second
    pygame.display.flip()
    clock.tick(60)

# Close the window and quit.
pygame.quit()