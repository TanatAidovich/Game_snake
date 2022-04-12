import pygame
from config.config import window, TILE


class Point:
    def __init__(self, collor, coordinats):
        self.collor = collor
        self.tile = pygame.Rect(*coordinats, TILE, TILE)

    def draw(self):
        pygame.draw.rect(window, self.collor, self.tile)
