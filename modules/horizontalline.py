from modules.point import Point
from modules.figure import Figure
from config.config import WIDTH, TILE


class HorizontalLine(Figure):

    def __init__(self, color, start, duration, line_number):

        for i in range(duration):
            Figure.points.append(
                Point(color, ((start - 1 + i) * TILE, (line_number - 1) * TILE)))
