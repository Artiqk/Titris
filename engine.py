def block_position_valid(x, y, board):
    return (board.board[x][y] == '.')


def blocks_positions_valid(blocks_coordinates, x, y, board):
    for i in range(len(blocks_coordinates)):
        block_x = x + blocks_coordinates[i][0]
        block_y = y - blocks_coordinates[i][1]
        if not block_position_valid(block_x, block_y, board):
            return False
    return True


def get_completed_rows(board):
    completed_rows = []

    for y in range(board.height):
        blocks_count = 0
        for x in range(board.width):
            if type(board.board[x][y]) is dict:
                blocks_count += 1
        if blocks_count == board.width:
            completed_rows.append(y)
    return completed_rows[::-1]


def remove_row(row, shapes):
    for shape in shapes:
        blocks = shape.blocks
        height = shape.height
        for block in blocks:
            shape_row = block[1]
            y = shape.y - shape_row
            if y == row:
                row_to_remove = (height - shape_row) - 1
                remove_shape_row(shape, row_to_remove)
                shape.update_blocks()


def remove_shape_row(shape, row_to_remove):
    width = shape.width
    for i in range(width):
        shape.shape[row_to_remove][i] = 0



def remove_empty_shapes(shapes):
    shapes_to_remove_index = []
    for i in range(len(shapes)):
        if len(shapes[i].blocks) == 0:
            shapes_to_remove_index.append(i)
    shapes_to_remove_index = shapes_to_remove_index[::-1]
    for index in shapes_to_remove_index:
        del shapes[index]


def fall_shapes(shapes, board):
    shape_moved = False
    for shape in shapes:
        below_y = shape.y - shape.blocks[-1][1] + 1
        if (below_y < board.height):
            below_block = board.board[shape.x][below_y]
            if (below_block == '.'):
                shape.move(0, 1)
                shape_moved = True
    return shape_moved