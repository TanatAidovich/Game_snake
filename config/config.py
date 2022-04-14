import pygame

pygame.init()

TILE = 7
WIDTH, HEIGHT = 120, 80
FPS = 60
BORDER_COLOR = 'springgreen3'


class Directions:

    right = 0
    left = 1
    up = 2
    down = 3


DIRECTIONS = Directions()


window = pygame.display.set_mode((WIDTH * TILE, HEIGHT * TILE))
clock = pygame.time.Clock()
