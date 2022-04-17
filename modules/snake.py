from modules.figure import Figure
from modules.point import Point
from config.config import TILE


class Snake(Figure):

    def __init__(self, color, tail_coordinats, length, direction):
        x, y = tail_coordinats
        x, y = x * TILE, y * TILE
        dir_x, dir_y = direction
        for i in range(length):
            _x = x + TILE * dir_x * i
            _y = y + TILE * dir_y * i
            Figure.points.append(Point(color, (_x, _y)))
