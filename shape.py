
class Shape:

    def __init__(self, shape):
        self.shape = shape
        self.width, self.height = self.get_sizes()
        self.x, self.y = self.get_origin()


    def get_sizes(self):
        height = len(self.shape)
        width  = len(self.shape[0])
        return width, height


    def get_origin(self):
        x = 0
        y = len(self.shape) - 1
        return x, y


    def get_all_coordinates(self):
        origin_x, origin_y = self.x, self.y
        coordinates = []
        
        for y in range(self.height):
            for x in range(self.width):
                if self.shape[y][x] == 1:
                    coordinates.append((abs(origin_x - x), abs(origin_y - y)))
        
        return coordinates
