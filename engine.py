def insert_shape_on_board(shape, board, x, y):
    blocks_coordinates = shape.get_all_coordinates()

    can_be_placed = blocks_positions_valid(blocks_coordinates, x, y, board)

    if can_be_placed:
        for i in range(len(blocks_coordinates)):
            block_x = x + blocks_coordinates[i][0]
            block_y = y - blocks_coordinates[i][1]
            board.board[block_x][block_y] = 1
    

def block_position_valid(x, y, board):
    return (board.board[x][y] == '.')


def blocks_positions_valid(blocks_coordinates, x, y, board): # FIXME - DRY ? 
    for i in range(len(blocks_coordinates)):
        block_x = x + blocks_coordinates[i][0]
        block_y = y - blocks_coordinates[i][1]
        if not block_position_valid(block_x, block_y, board):
            return False
    return True