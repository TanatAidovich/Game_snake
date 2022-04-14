class Figure:

    points = []

    def draw(self):
        for point in Figure.points:
            point.draw()
