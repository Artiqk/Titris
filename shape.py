
class Shape:

    def __init__(self, shape, x, y, color):
        self.shape = shape
        self.width, self.height = self.get_sizes()
        self.origin_x, self.origin_y = self.get_origin()
        self.x = x
        self.y = y
        self.color = color
        self.blocks = self.update_blocks()


    def get_sizes(self):
        height = len(self.shape)
        width  = len(self.shape[0])
        return width, height


    def get_origin(self):
        x = 0
        y = len(self.shape) - 1
        return x, y


    def update_blocks(self):
        origin_x, origin_y = self.origin_x, self.origin_y
        coordinates = []
        
        for y in range(self.height):
            for x in range(self.width):
                if self.shape[y][x] == 1:
                    coordinates.append((abs(origin_x - x), abs(origin_y - y)))
        
        return coordinates


    def move(self, offset_x, offset_y):
        self.x += offset_x
        self.y += offset_y
        self.blocks = self.update_blocks()
