import pygame
from constants import *

x_spawn = 500
y_spawn = 750
player_rect = pygame.Rect(x_spawn, y_spawn, 32, 32)
player_color = RED
speed = 5


def player_move(speed):
    global player_rect
    if pygame.key.get_pressed()[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.left -= speed
    elif pygame.key.get_pressed()[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.right += speed
    elif pygame.key.get_pressed()[pygame.K_UP] and player_rect.top > 0:
        player_rect.top -= speed
    elif pygame.key.get_pressed()[pygame.K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect.bottom += speed
    return player_rect


def player_attack():
    global player_color
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        player_color = GREEN
    else:
        player_color = RED
    return player_color


def life_status(coord):
    life = pygame.Rect(coord[0], coord[1] - 10, 30, 5)
    return life