import pygame

pygame.init()

TILE = 5
WIDTH, HEIGHT = 120, 80
FPS = 60


window = pygame.display.set_mode((WIDTH * TILE, HEIGHT * TILE))
clock = pygame.time.Clock()
