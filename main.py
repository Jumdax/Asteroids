import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
    # Initialize pygame
    pygame.init()

    # Create a GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create groups for updatable and drawable objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

     # Add Player and Asteroid classes to the appropriate groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    # Create a Clock object and initialize dt
    clock = pygame.time.Clock()
    dt = 0

    # Instantiate the player in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    # Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game loop and terminate the program

        # Update all objects in the updatable group
        for obj in updatable:
            obj.update(dt)
        
        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                return  # Exit the game loop and terminate the program

        # Draw all objects in the drawable group
        screen.fill((0, 0, 0))  # Fill screen with black
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()  # Refresh the screen

        # Control the frame rate and calculate delta time
        dt = clock.tick(60) / 1000  # Tick returns milliseconds; convert to seconds

    pygame.quit()


if __name__ == "__main__":
    main()


