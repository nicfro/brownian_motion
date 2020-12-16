import pygame
import numpy as np
import math
import particles
from config import settings
from collections import defaultdict
import collider
import random
from color_helper import Color_helper
import spawner

BLACK = (0, 0, 0)
pygame.init()
 
# Set the width and height of the screen [width, height]
size = [settings["x_boundary"], settings["y_boundary"]]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Brownian Motion")

done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
particles_array = []

particles_array = spawner.Spawner().particles
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    collider.Collide(particles = particles_array)

    for particle in particles_array:
        pygame.draw.circle(color=particle.color, surface=screen, center=particle.position, radius=particle.radius)
        particle.update_position()
    
    # --- Limit to 60 frames per second
    pygame.display.flip()
    clock.tick(60)

# Close the window and quit.
pygame.quit()