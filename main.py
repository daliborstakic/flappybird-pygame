import pygame

pygame.init()

# Constant variables
WIDTH = 300
HEIGHT = 600

# Setting up the screen
surf = pygame.display.set_mode((WIDTH, HEIGHT))

# Game clock
clock = pygame.time.Clock()
FPS = 60


# Function dedicated to rendering and drawing objects
def render():
    pygame.display.update()


# Game loop
def main():
    while True:
        clock.tick(FPS)

        for event in pygame.event:
            if event.type == pygame.QUIT:
                pygame.quit()

        render()


main()
