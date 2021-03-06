import pygame
from player import *
from constants import *

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
run = True

while run:
    screen.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    pygame.draw.rect(screen, player_attack(), player_move(speed))
    pygame.draw.rect(screen, GREEN, life_status((player_rect[0], player_rect[1])))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
