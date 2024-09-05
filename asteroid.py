import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        right_vector = self.velocity.rotate(random_angle)
        left_vector = self.velocity.rotate(-random_angle)
        right_asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        right_asteroid.velocity = right_vector * 1.2
        left_asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        left_asteroid.velocity = left_vector * 1.2
        
