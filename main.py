# Import pygame and constants
import pygame
from constants import *

def main():
    # Initialize pygame
    pygame.init()

    # Create a GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game loop and terminate the program

        # Fill the screen with black
        screen.fill((0, 0, 0))  # RGB color for black

        # Refresh the screen
        pygame.display.flip()

    # Quit pygame (this will be executed after exiting the loop)
    pygame.quit()

if __name__ == "__main__":
    main()


