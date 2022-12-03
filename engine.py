def block_position_valid(x, y, board):
    return (board.board[x][y] == '.')


def blocks_positions_valid(blocks_coordinates, x, y, board):
    for i in range(len(blocks_coordinates)):
        block_x = x + blocks_coordinates[i][0]
        block_y = y - blocks_coordinates[i][1]
        if not block_position_valid(block_x, block_y, board):
            return False
    return True


def get_completed_rows(board): # FIXME - reverse completed rows
    completed_rows = []

    for y in range(board.height):
        blocks_count = 0
        for x in range(board.width):
            if type(board.board[x][y]) is dict:
                blocks_count += 1
        if blocks_count == board.width:
            completed_rows.append(y)
    return completed_rows

def is_row_complete(row, board):
    return row in get_completed_rows(board)

def remove_row(row, shapes):
    for shape in shapes:
        if row == shape.y:
            del shape.shape[-1]

