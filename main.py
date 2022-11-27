from board import *
from shape import *
from engine import *
from shapes_data import *

from time import sleep
from os import system

def game():
    system("clear||cls")
    board.update()
    board.display()
    sleep(1)

board = Board(10, 20)

shape_z = Shape(z)
shape_angle = Shape(angle_bot_left)
shape_l = Shape(l_right)


game()

insert_shape_on_board(shape_z, board, 4, 19)
game()

insert_shape_on_board(shape_angle, board, 1, 19)
game()

insert_shape_on_board(shape_l, board, 7, 19)
game()

shape_z.y -= 2
game()