import pygame
from config.config import window, TILE, DIRECTIONS


class Point:
    def __init__(self, color, coordinats):
        self.color = color
        self.coordinats = coordinats
        self.tile = pygame.Rect(*self.coordinats, TILE, TILE)

    def draw(self):
        pygame.draw.rect(window, self.color, self.tile)

    def move(self, direction):
        if direction == DIRECTIONS.right:
            self.coordinats = (self.coordinats[0] + TILE, self.coordinats[1])
        elif direction == DIRECTIONS.left:
            self.coordinats = (self.coordinats[0] - TILE, self.coordinats[1])
        elif direction == DIRECTIONS.up:
            self.coordinats = (self.coordinats[0], self.coordinats[1] - TILE)
        elif direction == DIRECTIONS.down:
            self.coordinats = (self.coordinats[0], self.coordinats[1] + TILE)
