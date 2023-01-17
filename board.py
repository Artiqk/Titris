from termcolor import colored
import copy

class Board:

    def __init__(self, map_type):
        self.map_type = map_type
        self.width = len(map_type[0])
        self.height = len(map_type)
        self.board = self.generate_board(map_type)
    

    def generate_board(self, map_type):
        board = copy.deepcopy(map_type)
        for y in range(self.height):
            for x in range(self.width):
                if board[y][x] == 1:
                    board[y][x] = '.'
        return board


    def display(self):
        for i in range(self.width):
            print(chr(i + 97), end=' ')
        print()
        for y in range(self.height):
            for x in range(self.width):
                element = self.board[y][x]
                if type(element) is dict: # Si l'élèment est un dictionnaire, alors c'est un bloc d'une shape
                    print(colored(element["content"], element["color"]), end=' ')
                elif element == 2:
                    print(" ", end=' ')
                else:
                    print(element, end=' ')
            print(chr(y + 65))
        print() 


    def update(self, shapes):
        solid_square = chr(int('0x25A0', 0)) # Hex for solid square unicode character
        self.board = self.generate_board(self.map_type)
        for shape in shapes:
            for coordinates in shape.blocks:
                x = shape.x + coordinates[0]
                y = shape.y - coordinates[1]
                self.board[y][x] = {
                    "content": solid_square,
                    "color": shape.color
                }