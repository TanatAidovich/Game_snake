import pygame
from config.config import *
from modules.point import Point
from modules.horizontalline import HorizontalLine

test_point = Point('red', (200, 200))
test_horizontal_line = HorizontalLine('yellow', 25, 75, 75)

is_play = True

while is_play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_play = False

    test_horizontal_line.draw()
    test_point.draw()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
