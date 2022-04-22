from random import randint
import pygame
from config.config import BORDER_COLOR, WIDTH, HEIGHT, FPS, clock, DIRECTIONS, window
from modules.point import Point
from modules.horizontalline import HorizontalLine
from modules.verticalline import VerticalLine
from modules.snake import Snake

# test_point = Point('red', (200, 200))


border_bottom = HorizontalLine(BORDER_COLOR, 1, WIDTH, HEIGHT)
border_top = HorizontalLine(BORDER_COLOR, 1, WIDTH, 1)
border_right = VerticalLine(BORDER_COLOR, 1, HEIGHT, WIDTH)
border_left = VerticalLine(BORDER_COLOR, 1, HEIGHT, 1)

# snake_2 = Snake('green', (60, 40), 25, DIRECTIONS.up)
# snake_3 = Snake('red', (60, 40), 25, DIRECTIONS.down)
# snake_4 = Snake('blue', (60, 40), 25, DIRECTIONS.left)
# snake_5 = Snake('white', (60, 40), 25, DIRECTIONS.right)
test_point = Point('red', (5, 5))
test_point.set_coordinat_x(115)
test_point.set_coordinat_y(75)

is_play = True

while is_play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_play = False

    window.fill('black')
    border_bottom.draw()
    border_top.draw()
    border_right.draw()
    border_left.draw()
    test_point.draw()
    # test_point.move(randint(0, 3))
    # snake_2.draw()
    # snake_3.draw()
    # snake_4.draw()
    # snake_5.draw()
    pygame.display.update()
    clock.tick(FPS)


pygame.quit()
