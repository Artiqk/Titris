def insert_shape_on_board(shape, board, x, y):
    blocks_coordinates = shape.get_all_coordinates()
    for i in range(len(blocks_coordinates)):
        board.board[x + blocks_coordinates[i][0]][y - blocks_coordinates[i][1]] = "x"