import pygame
from player import *

WIDTH, HEIGHT = 1500, 1000
FPS = 60

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
run = True

player, color = player_spawn()

while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    pygame.draw.rect(screen, color, player)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()