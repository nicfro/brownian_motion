from particles import Particle

test_particle_1 = Particle(1)
test_particle_2 = Particle(2)
test_particle_3 = Particle(3)

def test_bounds():
    assert test_particle_1.right == test_particle_1.position[0] + 1
    assert test_particle_1.left == test_particle_1.position[0] - 1
    assert test_particle_1.top == test_particle_1.position[1] - 1
    assert test_particle_1.bottom == test_particle_1.position[1] + 1