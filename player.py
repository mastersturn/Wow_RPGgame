import pygame

def player_spawn():
    player_rect = pygame.Rect(500, 750, 50, 50)
    P_COLOR = (255, 0, 0)
    return player_rect, P_COLOR

def player_move():
