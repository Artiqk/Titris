from board import *
from shape import *
from engine import *
from shapes_data import *

from time import sleep
from os import system

system('color')

shapes = [
    Shape(z, 4, 19, "yellow"),
    Shape(angle_bot_left, 3, 19, "cyan"), 
    Shape(l_right, 7, 19, "green"),
    Shape(t_bot, 0, 19, "blue"),
    Shape(t_bot, 6, 18, "blue"),
    Shape(t_top, 1, 18, "blue"),
    Shape(i, 0, 18, "magenta"),
    Shape(square, 4, 17, "white"),
    Shape(i, 6, 18, "magenta"),
    Shape(square, 8, 17, "white")
]

def game(shapes):
    # system("clear||cls")
    board.update(shapes)
    board.display()
    system("pause")

board = Board(10, 20)

game(shapes)

for row in get_completed_rows(board):
    remove_row(row, shapes)
    game(shapes)

