from termcolor import colored

import math

from shape import *
from board import *
from game_shapes.default_shapes import *
from game_shapes.circle_shapes import *
from game_shapes.diamond_shapes import *
from game_shapes.triangle_shapes import *

from time import sleep
from os import system

import numpy as np
import random
import string


colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']


shape_settings = {
    "circle": circle_shapes,
    "diamond": diamond_shapes,
    "triangle": triangle_shapes
}


def block_position_valid(x, y, board):
    x_valid = x >= 0 and x < board.width
    y_valid = y >= 0 and y < board.height
    if not (x_valid and y_valid):
        return False
    return (board.board[y][x] == '.')


def shape_position_valid(shape, new_x, new_y, board):
    for block in shape.blocks:
        x = new_x + block[0]
        y = new_y - block[1]
        if not block_position_valid(x, y, board):
            return False
    return True


def get_completed_rows(board): # FIXME - Move to class Board ?
    completed_rows = []

    for y in range(board.height):
        blocks_count = 0
        for x in range(board.width):
            if type(board.board[y][x]) is dict or board.board[y][x] == 2:
                blocks_count += 1
        if blocks_count == board.width:
            completed_rows.append(y)
    return completed_rows[::-1]


def get_completed_columns(board):
    completed_columns = []
    width = len(board[0])
    height = len(board)

    for y in range(height):
        blocks_count = 0
        for x in range(width):
            if type(board[y][x]) is dict or board[y][x] == 2:
                blocks_count += 1
        if blocks_count == height:
            completed_columns.append(y)
            
    return completed_columns


def handle_shapes_fall(shapes, board):
    shapes.sort(key=lambda x: x.y, reverse=True)
    shape_moved = False
    for shape in shapes:
        if below_shape_free(shape, board):
            shape.move(0, 1)
            shape_moved = True
    return shape_moved



def below_shape_free(shape, board): # FIXME - Rename function
    bottom_block_y = shape.blocks[-1][1] # -1 -> dernier block de la liste. 1 -> y.
    inside_field = (shape.y - bottom_block_y + 1) < board.height
    if not inside_field:
        return False
    return all([below_block_free(block, shape, board) for block in shape.blocks])


def below_block_free(block, shape, board):
    block_x = shape.x + block[0]
    block_y = shape.y - block[1]
    below_y = block_y + 1

    if below_y >= board.height:
        return False

    below_y_block = board.board[below_y][block_x]
    
    if type(below_y_block) is dict:
        return is_block_from_shape(block_x, below_y, shape)
    
    if below_y_block == 2:
        return False

    return True


def is_block_from_shape(block_x, block_y, shape): # FIXME - Move to class Shape ? 
    for block in shape.blocks:
        x = shape.x + block[0]
        y = shape.y - block[1]
        if (x == block_x) and (y == block_y):
            return True
    return False



def draw_shapes_on_line(shapes, add_digits=True):
    solid_square = chr(int('0x25A0', 0))
    height = len(max(shapes, key=len))

    for i in range(height):
        for shape in shapes:
            if len(shape) >= height:
                for block in shape[len(shape) - height]:
                    if block == 1:
                        print(colored(solid_square, "white"), end=' ')
                    else:
                        print(' ', end=' ')
            else:
                print(' ' * (len(shape[0]) * 2), end='')
            print(' ', end=' ')
        print()
        height -= 1

    if (add_digits):
        for i in range(len(shapes)):
            print(str(i + 1) + '.', end='')
            print(' ' * (len(shapes[i][0]) * 2), end='')
    print()
    print()
                


def draw_shape(shape, color): # FIXME - Move to class Shape ? 
    solid_square = chr(int('0x25A0', 0))
    print()
    for row in shape:
        for block in row:
            if block == 1:
                print(colored(solid_square, color), end=' ')
            else:
                print(' ', end=' ')
        print()
    print()


def check_game_over(fail_counter):
    if fail_counter == 3:
        print("Game Over!")
        exit(1)


def get_shape_coords(shape, board):
    x = -1
    y = -1

    x_valid = False
    y_valid = False

    fail_counter = 0

    while not (x_valid and y_valid):
        coords = input("Entrez les coordonnées pour la pièce ci-dessus (aA): ")

        x = ord(coords[0].lower()) - 97
        y = ord(coords[1].upper()) - 65

        x_valid = x >= 0 and x < board.width
        y_valid = y >= 0 and y < board.height

        if not (x_valid and y_valid):
            fail_counter += 1
        
        check_game_over(fail_counter)

    return x, y


def get_next_shape(map_shape):
    next_shape = default_shapes[random.choice(list(default_shapes.keys()))]
    shape_color = random.choice(colors)
    return next_shape, shape_color


def choose_next_shape(map_shape, number_of_shapes=3): # Ce parametre permet de definir combien de shape on propose à l'utilisateur => par défaut il est à 3
    shapes_choice = []
    shapes_colors = []

    for i in range(number_of_shapes):
        next_shape, shape_color = get_next_shape(map_shape)
        shapes_choice.append(next_shape)
        shapes_colors.append(shape_color)

    draw_shapes_on_line(shapes_choice)
    chosen_shape = -1
    while chosen_shape < 1 or chosen_shape > number_of_shapes:
        chosen_shape = input(f"Choisissez la pièce que vous voulez utiliser (1-{number_of_shapes}) : ")
        if chosen_shape.isdigit(): # Cette condition gère une partie des entrées indésirables
            chosen_shape = int(chosen_shape)
        else: # Celle-là aussi
            chosen_shape = -1
    index = chosen_shape - 1
    return shapes_choice[index], shapes_colors[index]


def insert_new_shape(shapes, board, map_shape):
    fail_counter = 0
    position_valid = False
    shape, color = choose_next_shape(map_shape, 10)
    draw_shape(shape, color)

    while not position_valid:
        x, y = get_shape_coords(shape, board)
        new_shape = Shape(shape, x, y, color)

        if shape_position_valid(new_shape, x, y, board):
            shapes.append(new_shape)
            position_valid = True
        else:
            fail_counter += 1
        
        check_game_over(fail_counter)