from board import *
from shape import *
from engine import *
from default_shapes import *

from time import sleep
from os import system

system('color')

board = Board(10, 20)


def update(shapes):
    handle_completed_rows(shapes)
    board.update(shapes)


def game(shapes):
    system("clear||cls")
    update(shapes)
    board.display()
    sleep(0.1)


def handle_completed_rows(shapes):
    for row in get_completed_rows(board):
        remove_row(row, shapes)
    remove_empty_shapes(shapes)



# while fall_shapes(shapes, board):
#     game(shapes)