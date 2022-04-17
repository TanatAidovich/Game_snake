import pygame
from config.config import window, TILE, DIRECTIONS


class Point:
    def __init__(self, color, coordinats):
        self.color = color
        self.tile = pygame.Rect(*coordinats, TILE, TILE)

    def draw(self):
        pygame.draw.rect(window, self.color, self.tile)

    def move(self, direction):
        if direction == DIRECTIONS.right:
            self.tile.x += TILE
        elif direction == DIRECTIONS.left:
            self.tile.x -= TILE
        elif direction == DIRECTIONS.up:
            self.tile.y -= TILE
        elif direction == DIRECTIONS.down:
            self.tile.y += TILE
