from config import settings
import particles
import collider
import numpy as np
import random

class Spawner:
    def __init__(self):
        counter = 1
        self.particles = []
        
        for i in range(settings["number_of_particles"] * 2):
            #particle = particles.Particle(identifier = counter, radius = random.uniform(5, 20), density = random.uniform(1, 10))
            particle = particles.Particle(identifier = counter, radius = settings["small_particle_radius"])
            self.particles.append(particle)
            counter += 1
        self.particles = np.array(self.particles)
        overlaps = collider.Collide(particles = self.particles).get_collisions()
        deletes = [x[0] for x in overlaps]

        self.particles = list(np.delete(self.particles, deletes))

        if len(self.particles) > settings["number_of_particles"]:
            print(f"too many ({len(self.particles)}) down sampling")
            deletes = random.sample(self.particles, settings["number_of_particles"])
        else:
            print(f"could only fit {len(self.particles)} on screen")