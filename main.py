import pygame
import random

pygame.init()


# Bird class
class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    falling_speed = 3
    jump_force = 50


# Pole class
class Pole:
    def __init__(self, x, y1, y2):
        self.x = x
        self.y1 = y1
        self.y2 = y2

    move_speed = 5
    size_between = 30


# Constant variables
WIDTH = 300
HEIGHT = 500

# Colors
BLACK = (0, 0, 0)

# Setting up the screen
surf = pygame.display.set_mode((WIDTH, HEIGHT))

# Game clock
clock = pygame.time.Clock()
FPS = 60

# Images
BACKGROUND = pygame.image.load("Sprites/background.png")
GROUND = pygame.image.load("Sprites/ground.png")
BIRD_IMAGE = pygame.transform.scale2x(pygame.image.load("Sprites/bird.png"))
POLE_IMAGE = pygame.image.load("Sprites/pole.png")
POLE_IMAGE_ROTATED = pygame.image.load("Sprites/pole_rotated.png")

# Title and icon
pygame.display.set_caption("Flappy Bird")
pygame.display.set_icon(BIRD_IMAGE)


# Function dedicated to rendering and drawing objects
def render(pole):
    surf.fill(BLACK)
    surf.blit(BACKGROUND, (0, 0))
    surf.blit(POLE_IMAGE, (pole.x, pole.y1 - pole.size_between))
    surf.blit(POLE_IMAGE_ROTATED, (pole.x, pole.y2 + pole.size_between))
    surf.blit(GROUND, (0, HEIGHT - GROUND.get_height()))
    surf.blit(BIRD_IMAGE, (bird.x, bird.y))
    pygame.display.update()


# Game loop
def main():
    global bird

    poles = [Pole(WIDTH + POLE_IMAGE.get_width(), 0, HEIGHT / 2)]

    bird = Bird(20, (HEIGHT - GROUND.get_height() - BIRD_IMAGE.get_height()) // 2)

    while True:
        clock.tick(FPS)

        bird.y += bird.falling_speed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                bird.y -= bird.jump_force

        for pole in poles:

            pole.x -= pole.move_speed

            render(pole)

            if pole.x <= - POLE_IMAGE.get_width():
                poles.pop(0)
                poles.append(Pole(WIDTH + POLE_IMAGE.get_width(), 0, HEIGHT / 2))
                poles[0].size_between = random.randint(30, 55)

        bird.y = bird.y if bird.y >= 0 else 0


main()
