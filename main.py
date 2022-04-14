from random import randint
import pygame
from config.config import BORDER_COLOR, WIDTH, HEIGHT, FPS, clock, DIRECTIONS
from modules.point import Point
from modules.horizontalline import HorizontalLine
from modules.verticalline import VerticalLine
from pygame.color import THECOLORS

test_point = Point('red', (200, 200))


border_bottom = HorizontalLine(BORDER_COLOR, 1, WIDTH, HEIGHT)
border_top = HorizontalLine(BORDER_COLOR, 1, WIDTH, 1)
border_right = VerticalLine(BORDER_COLOR, 1, HEIGHT, WIDTH)
border_left = VerticalLine(BORDER_COLOR, 1, HEIGHT, 1)




is_play = True

while is_play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_play = False

    border_bottom.draw()
    border_top.draw()
    border_right.draw()
    border_left.draw()
    test_point.draw()
    test_point.move(randint(0,3))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
