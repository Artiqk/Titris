import copy

class Shape:

    def __init__(self, shape, x, y, color):
        self.shape = copy.deepcopy(shape)
        self.width, self.height = self.get_sizes()
        self.origin_x, self.origin_y = self.get_origin()
        self.x = x
        self.y = y
        self.color = color
        self.update_blocks()


    def __str__(self):
        return str(self.x) + ':' + str(self.y) + '  ' + self.color

    def get_sizes(self):
        height = len(self.shape)
        width  = len(self.shape[0])
        return width, height


    def get_origin(self):
        x = 0
        y = len(self.shape) - 1
        return x, y


    def update_blocks(self):
        coordinates = []

        for i in range(len(self.shape) - 1, -1, -1):
            if all(self.shape[i][j] == 0 for j in range(len(self.shape[i]))):
                del self.shape[i]

        if len(self.shape) > 0:
            self.width, self.height = self.get_sizes()
            
            self.origin_x, self.origin_y = self.get_origin()
            
            for y in range(self.height):
                for x in range(self.width):
                    if self.shape[y][x] == 1:
                        coordinates.append((abs(self.origin_x - x), abs(self.origin_y - y)))

        self.blocks = coordinates


    def move(self, offset_x, offset_y):
        self.x += offset_x
        self.y += offset_y
        self.update_blocks()