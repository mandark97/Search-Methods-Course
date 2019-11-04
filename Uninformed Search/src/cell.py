class Cell(object):
    def __init__(self, x, y, dist=0, road=[]):
        self.x = x
        self.y = y
        self.dist = dist
        self.road = road.copy()
        self.road.append(self)

    def __eq__(self, cell):
        if cell:
            return self.x == cell.x and self.y == cell.y
        # else:
        #     return

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.dist})"

    def move(self, movement):
        x, y = movement
        return Cell(self.x + x, self.y + y, self.dist + 1, self.road)

    def is_valid(self, dim, visited):
        return self.x >= 0 and self.x < dim and \
            self.y >= 0 and self.y < dim and \
            visited[self.x][self.y] == None
