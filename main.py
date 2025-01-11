import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    # Initialize pygame
    pygame.init()

    # Create a GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create groups for updatable and drawable objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Add Player class to both groups
    Player.containers = (updatable, drawable)

    # Create a Clock object and initialize dt
    clock = pygame.time.Clock()
    dt = 0

    # Instantiate the player in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game loop and terminate the program

        # Update all objects in the updatable group
        for obj in updatable:
            obj.update(dt)

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


