from modules.point import Point
from modules.figure import Figure

class VerticalLine(Figure):

    def __init__(self, color, start, duration, column_number):

        for i in range(duration):
            Figure.points.append(
                Point(color, (column_number - 1, start - 1 + i)))
