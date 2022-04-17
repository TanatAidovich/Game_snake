import pygame

pygame.init()

TILE = 7
WIDTH, HEIGHT = 120, 80
FPS = 60
BORDER_COLOR = 'springgreen3'


class Directions:

    right = [1, 0]
    left = [-1, 0]
    up = [0, -1]
    down = [0, 1]


DIRECTIONS = Directions()


window = pygame.display.set_mode((WIDTH * TILE, HEIGHT * TILE))
clock = pygame.time.Clock()
