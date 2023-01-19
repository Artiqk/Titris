from engine import *
from maps import *
from main_menu import *

map_settings = {
    "circle": circle,
    "diamond": diamond,
    "triangle": triangle
}

os.system("cls||clear")

map_shape, pol_shape = menu()

map_type = map_settings[map_shape]

system('color')

seed = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))

random.seed(seed)

board = Board(map_type)

shapes = []

score = 0

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


def draw():
    system("clear||cls")
    print("===============")
    print(f" Score: {score}")
    print("===============")
    board.display()
    sleep(0.05)



def loop():
    global score

    while handle_shapes_fall(shapes, board):
        board.update(shapes)
        draw()

    completed_rows = get_completed_rows(board)

    if len(completed_rows) > 0:
        for row in completed_rows:
            remove_row(row, shapes)
            score += 100
        for shape in shapes:
            shape.update_blocks()
        remove_empty_shapes(shapes)
    else:
        insert_new_shape(shapes, board, map_shape, score, pol_shape)

    board.update(shapes)
    draw()


best_player, best_score = get_player_best_score("score.txt")

print(f"Le meilleur joueur est {best_player} avec un score de {best_score} points !")

draw()

while 1:
    loop()
