import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # Draw the asteroid as a circle
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        # Move the asteroid in a straight line
        self.position += self.velocity * dt

    def split(self):
        # Kill the current asteroid
        self.kill()

        # If this asteroid is small, don't split further
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Calculate the new radius for the smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Generate a random angle for splitting
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors
        velocity1 = self.velocity.rotate(random_angle) * 1.2  # Slightly faster
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        # Spawn two new asteroids at the current position with the new radius
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Set their velocities
        asteroid1.velocity = velocity1
        asteroid2.velocity = velocity2