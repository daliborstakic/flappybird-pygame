import pygame
import random
import tkinter
from tkinter import messagebox
from pygame import mixer

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
YELLOW = (100, 78, 14)
WHITE = (255, 255, 255)

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

# Fonts
SCORE_FONT = pygame.font.SysFont('arial', 20)


# Function dedicated to rendering and drawing objects
def render(pole, score_text):
    surf.fill(BLACK)
    surf.blit(BACKGROUND, (0, 0))
    surf.blit(POLE_IMAGE, (pole.x, pole.y1 - pole.size_between))
    surf.blit(POLE_IMAGE_ROTATED, (pole.x, pole.y2 + pole.size_between))
    surf.blit(GROUND, (0, HEIGHT - GROUND.get_height()))
    surf.blit(BIRD_IMAGE, (bird.x, bird.y))
    surf.blit(score_text, (10, 10))
    pygame.display.update()


def restart_game():
    global poles, bird, score
    score = 0
    poles = []
    poles = [Pole(WIDTH + POLE_IMAGE.get_width(), 0, HEIGHT / 2)]
    bird = Bird(20, (HEIGHT - GROUND.get_height() - BIRD_IMAGE.get_height()) // 2)
    pygame.time.delay(1000)


# Displays a message using the Tkinter module
def message_box(subject, content):
    root = tkinter.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)

    try:
        root.destroy()
    except:
        pass


# Handling the collision
def has_collided(pole):
    if (pole.x <= bird.x <= pole.x + POLE_IMAGE.get_width()) and (
            bird.y <= pole.y1 - pole.size_between + POLE_IMAGE.get_height() or bird.y >= pole.y2 + pole.size_between):
        return True
    return False


# Game loop
def main():
    global bird, poles, score

    poles = [Pole(WIDTH + POLE_IMAGE.get_width(), 0, HEIGHT / 2)]

    # Score parameters
    score = 0
    score_update = True

    bird = Bird(20, (HEIGHT - GROUND.get_height() - BIRD_IMAGE.get_height()) // 2)

    while True:
        clock.tick(FPS)

        score_text = SCORE_FONT.render("Score: {}".format(str(score)), 1, BLACK)

        bird.y += bird.falling_speed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                bird.y -= bird.jump_force

        for pole in poles:
            pole.x -= pole.move_speed

            pole.move_speed = (score // 10) + 5

            render(pole, score_text)

            if has_collided(pole):
                pygame.time.delay(500)
                message_box("You lost!", "Play again?")
                restart_game()
                break

            if bird.x >= pole.x and score_update:
                score += 1
                score_update = False

            if pole.x <= - POLE_IMAGE.get_width():
                poles.pop(0)
                score_update = True
                poles.append(Pole(WIDTH + POLE_IMAGE.get_width(), 0, HEIGHT / 2))
                poles[0].size_between = random.randint(30, 45)

        bird.y = bird.y if bird.y >= 0 else 0

if __name__ == '__main__':
    main()
