import pygame
from circleshape import CircleShape
from constants import *


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0  # in degrees

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt
        # Remove the shot if it goes off-screen
        if (self.position.x < 0 or self.position.x > SCREEN_WIDTH or
            self.position.y < 0 or self.position.y > SCREEN_HEIGHT):
            self.kill()