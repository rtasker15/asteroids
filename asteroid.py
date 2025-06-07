import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, position, velocity, radius):
        super().__init__(position.x, position.y, radius)

        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt


    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            rand_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            print("self.velocity")
            print(self.velocity)

            new_velocity_1 = pygame.Vector2(self.velocity).rotate(rand_angle) * 1.2
            new_velocity_2 = pygame.Vector2(self.velocity).rotate(-rand_angle) * 1.2

            print("new_velocity_1")
            print(new_velocity_1)
            print("new_velocity_2")
            print(new_velocity_2)

            new_asteroid_1 = Asteroid(self.position, new_velocity_1, new_radius)
            new_asteroid_2 = Asteroid(self.position, new_velocity_2, new_radius)

            print("Asteroid object velocity")
            print(new_asteroid_1.velocity)

            self.kill()
