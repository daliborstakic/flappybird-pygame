import pygame

pygame.init()

# Constant variables
WIDTH = 300
HEIGHT = 500

# Colors
BLACK = (0, 0, 0)

# Setting up the screen
surf = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Game clock
clock = pygame.time.Clock()
FPS = 60

# Images
BACKGROUND = pygame.image.load("Sprites/background.png")
BIRD_IMAGE = pygame.transform.scale2x(pygame.image.load("Sprites/bird.png"))


# Function dedicated to rendering and drawing objects
def render():
    surf.fill(BLACK)
    surf.blit(BACKGROUND, (0, 0))
    surf.blit(BIRD_IMAGE, (20, (HEIGHT - BIRD_IMAGE.get_height()) / 2))
    pygame.display.update()


# Game loop
def main():
    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        render()


main()
