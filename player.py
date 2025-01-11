import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN


class Player(CircleShape):
    def __init__(self, x, y):
        # Call the parent class constructor with x, y, and PLAYER_RADIUS
        super().__init__(x, y, PLAYER_RADIUS)

        self.shoot_timer = 0 # Timer for shooting cooldown
        self.rotation = 0 # Initialize the rotation field

    def triangle(self):
        # Define the points for the triangle shape of the player
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # Draw the player as a white triangle
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt, direction=1):
        # Move the player in the direction they are facing
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * direction
    
    def shoot(self):
        if self.shoot_timer <= 0:  # Check if cooldown has expired
            # Create a new shot at the player's position
            shot = Shot(self.position.x, self.position.y)
            
            # Set the velocity of the shot
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            shot.velocity = forward * PLAYER_SHOOT_SPEED

            # Reset the shooting cooldown
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):

        # Decrease the shoot timer
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:  # Rotate left
            self.rotate(-dt)  # Invert dt to rotate in the opposite direction
        if keys[pygame.K_d]:  # Rotate right
            self.rotate(dt)
        if keys[pygame.K_w]:  # Move forward
            self.move(dt, direction=1)
        if keys[pygame.K_s]:  # Move backward
            self.move(dt, direction=-1)
        if keys[pygame.K_SPACE]:  # Shoot Bullets
            self.shoot()