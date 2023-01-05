from termcolor import colored

def block_position_valid(x, y, board):
    x_valid = x >= 0 and x < board.width
    y_valid = y >= 0 and y < board.height
    if not (x_valid and y_valid):
        return False
    return (board.board[x][y] == '.')


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
    


def remove_shape_row(shape, row_to_remove): # FIXME - Move to class Shape ? 
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

    below_y_block = board.board[block_x][below_y]
    
    if type(below_y_block) is dict:
        return is_block_from_shape(block_x, below_y, shape)
    
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