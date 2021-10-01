import pygame

from core.soldier import Soldier

clock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
BG_COLOR = (144, 201, 120)
FPS = 60

moving_left = False
moving_right = False

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Soldier(screen, 200, 200, 3, 5)
pygame.display.set_caption("Shooty")


def draw_bg():
    screen.fill(BG_COLOR)


run = True

while run:
    draw_bg()

    clock.tick(FPS)

    player.draw()
    player.move(moving_left, moving_right)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True

            if event.key == pygame.K_d:
                moving_right = True

            if event.key == pygame.K_ESCAPE:
                run = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False

            if event.key == pygame.K_d:
                moving_right = False

    pygame.display.update()

pygame.quit()