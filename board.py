

class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.create_board()
    
    def create_board(self):
        board = []
        row = ['*'] * self.width
        for y in range(self.height):
            board.append(row)
        self.board = board
