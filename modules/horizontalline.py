from modules.point import Point
from modules.figure import Figure


class HorizontalLine(Figure):

    def __init__(self, color, start, duration, line_number):

        for i in range(duration):
            Figure.points.append(
                Point(color, (start - 1 + i, line_number - 1)))
