def block_position_valid(x, y, board):
    return (board.board[x][y] == '.')


def blocks_positions_valid(blocks_coordinates, x, y, board):
    for i in range(len(blocks_coordinates)):
        block_x = x + blocks_coordinates[i][0]
        block_y = y - blocks_coordinates[i][1]
        if not block_position_valid(block_x, block_y, board):
            return False
    return True