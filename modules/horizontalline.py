from modules.point import Point
from config.config import WIDTH, TILE


class HorizontalLine:

    def __init__(self, collor, start, finish, y):
        self.points = []
        for i in range(finish * TILE - start * TILE):
            self.points.append(Point(collor, (start + i * TILE, y * TILE)))

    def draw(self):
        for point in self.points:
            point.draw()
