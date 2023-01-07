from termcolor import colored

class Board:

    def __init__(self, width, height):
        self.width  = width
        self.height = height
        self.board = self.create_empty()
    

    def create_empty(self):
        board = []
        for x in range(self.width):
            row = []
            for y in range(self.height):
                row.append('.')
            board.append(row)
        return board


    def display(self):
        for i in range(self.width):
            print(chr(i + 97), end=' ')
        print()
        for y in range(self.height):
            for x in range(self.width):
                element = self.board[x][y]
                if type(element) is dict: # Si l'élèment est un dictionnaire, alors c'est un bloc d'une shape
                    print(colored(element["content"], element["color"]), end=' ')
                else:
                    print(element, end=' ')
            print(chr(y + 65))
        print()  

    def update(self, shapes):
        solid_square = chr(int('0x25A0', 0)) # Hex for solid square unicode character
        self.board = self.create_empty()
        for shape in shapes:
            for coordinates in shape.blocks:
                x = shape.x + coordinates[0]
                y = shape.y - coordinates[1]
                self.board[x][y] = {
                    "content": solid_square,
                    "color": shape.color
                }