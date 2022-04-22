import pygame
from config.config import window, TILE


class Point:

    def __init__(self, color, coordinats):
        self.color = color
        x, y = coordinats
        x, y = x * TILE, y * TILE
        self.tile = pygame.Rect(x, y, TILE, TILE)

    def draw(self):
        pygame.draw.rect(window, self.color, self.tile)

    def set_coordinat_x(self, x):
        self.tile.x = x * TILE

    def set_coordinat_y(self, y):
        self.tile.y = y * TILE
