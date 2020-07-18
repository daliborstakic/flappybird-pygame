import pygame

pygame.init()


# Bird class
class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    falling_speed = 3
    jump_force = 50


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
    surf.blit(BIRD_IMAGE, (bird.x, bird.y))
    pygame.display.update()


# Game loop
def main():
    global bird

    bird = Bird(20, (HEIGHT - BIRD_IMAGE.get_height()) // 2)

    while True:
        clock.tick(FPS)

        bird.y += bird.falling_speed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                bird.y -= bird.jump_force

        bird.y = bird.y if bird.y >= 0 else 0

        render()


main()
