from modules.figure import Figure
from modules.point import Point


class Snake(Figure):

    def __init__(self, color, tail_coordinats, length, direction):

        for i in range(length):
            point = Point(color, tail_coordinats)

            for _ in range(i):
                point.move(direction)

            Figure.points.append(point)

    # def move(self, direction):
    #     if direction == DIRECTIONS.right:
    #         self.tile.x += TILE
    #     elif direction == DIRECTIONS.left:
    #         self.tile.x -= TILE
    #     elif direction == DIRECTIONS.up:
    #         self.tile.y -= TILE
    #     elif direction == DIRECTIONS.down:
    #         self.tile.y += TILE
