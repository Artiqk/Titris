

class Board:

    def __init__(self, width, height):
        self.width  = width
        self.height = height
        self.create()
    

    def create(self):
        board = []
        for x in range(self.width):
            row = []
            for y in range(self.height):
                row.append('.')
            board.append(row)
        self.board = board


    def display(self):
        for i in range(self.width):
            print(i, end=' ')
        print()
        for y in range(self.height):
            for x in range(self.width):
                print(self.board[x][y], end=' ')
            print(y)
        print()

    def update(self):
        characters = {
            0: '.',
            1: chr(int('0x25A0', 0)) # Hex for solid square unicode character
        }
        board = self.board
        for y in range(self.height):
            for x in range(self.width):
                case = self.board[x][y]
                if case in characters:
                   self.board[x][y] = characters[case]