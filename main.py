from board import *
from shape import *
from engine import *
from default_shapes import *

from time import sleep
from os import system

import random
import string

system('color')

seed = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
random.seed(seed)

board = Board(10, 20)

shapes = []

colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']


def update(shapes):
    handle_completed_rows(shapes)
    board.update(shapes)


def handle_completed_rows(shapes):
    for row in get_completed_rows(board):
        remove_row(row, shapes)
    remove_empty_shapes(shapes)


def get_next_shape():
    next_shape = default_shapes[random.choice(list(default_shapes.keys()))]
    shape_color = random.choice(colors)
    return next_shape, shape_color


def check_game_over(fail_counter):
    if fail_counter == 3:
        print("Game Over!")
        exit(1)


def get_shape_coords():
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


def game(shapes):
    system("clear||cls")
    update(shapes)
    board.display()
    sleep(0.1)


def choose_next_shape(number_of_shapes=3): # Ce parametre permet de definir combien de shape on propose à l'utilisateur => par défaut il est à 3
    shapes_choice = []
    shapes_colors = []

    for i in range(number_of_shapes):
        next_shape, shape_color = get_next_shape()
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


def new_shape_step():
    fail_counter = 0
    position_valid = False
    shape, color = choose_next_shape(5)
    draw_shape(shape, color)

    while not position_valid:
        x, y = get_shape_coords()
        new_shape = Shape(shape, x, y, color)

        if shape_position_valid(new_shape, x, y, board):
            shapes.append(new_shape)
            position_valid = True
        else:
            fail_counter += 1
        
        check_game_over(fail_counter)


def draw():
    system("clear||cls")
    board.display()


def loop():
    new_shape_step()

    board.update(shapes)

    handle_completed_rows(shapes)

    board.update(shapes)
    draw()

    while fall_shapes(shapes, board):
        board.update(shapes)
        draw()


draw()
while 1:
    loop()



















# def loop():
#     next_shape, shape_color = get_next_shape()
#     draw_shape(next_shape, shape_color)

#     x, y = get_shape_coords()
#     shapes.append(Shape(next_shape, x, y, shape_color))

#     update(shapes)

#     completed_rows = get_completed_rows(board)

#     if len(completed_rows) > 0:
#         handle_completed_rows(shapes)

#     update(shapes)
    
#     while fall_shapes(shapes, board):
#         game(shapes)

#     game(shapes)


# board.display()

# for i in range(100):
#     loop()



# while fall_shapes(shapes, board):
#     game(shapes)