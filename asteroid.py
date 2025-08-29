from circleshape import *
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0  # in degrees

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            # Create two smaller asteroids
            for _ in range(2):
                new_radius = self.radius / 2
                new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
                new_speed = random.randint(40, 100)
                new_velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize() * new_speed
                new_asteroid.velocity = new_velocity
                self.containers[0].add(new_asteroid)
        self.kill()