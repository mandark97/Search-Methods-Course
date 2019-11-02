from cell import Cell


MOVEMENTS = [(2, 1), (2, -1), (-2, 1), (-2, -1),
             (1, 2), (1, -2), (-1, 2), (-1, -2)]


class Counter:
    # wraps a function, to keep a running count of how many
    # times it's been called
    def __init__(self, func):
        self.func = func
        self.count = count

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)


class BFS(object):
    def __init__(self, dim, visit_matrix=None):
        self.dim = dim
        self.queue = []

        if visit_matrix:
            self.visited = visit_matrix
        else:
            self.visited = [[None for i in range(dim)] for j in range(dim)]

    def run(self, src, dest):
        self.initialize_run(src)

        while len(self.queue) > 0:
            current_cell = self.queue.pop(0)
            if current_cell == dest:
                return current_cell
            self.step(current_cell)
        print("ended")

    def initialize_run(self, src):
        self.visited[src.x][src.y] = src
        self.queue.append(src)

    def step(self, current_cell=None):
        for movement in MOVEMENTS:
            new_cell = current_cell.move(movement)
            if new_cell.is_valid(self.dim, self.visited):
                self.visited[new_cell.x][new_cell.y] = new_cell
                self.queue.append(new_cell)

    # def __visit(self, new_cell):
    def __full_search(self):
        return all([all(row) for row in self.visited])


class BidirectionalSearch(object):
    def __init__(self, dim):
        self.bfs1 = BFS(dim)
        self.bfs2 = BFS(dim)

    def run(self, src, dest):
        self.bfs1.initialize_run(src)
        self.bfs2.initialize_run(dest)
        while True:
            if len(self.bfs1.queue) < len(self.bfs2.queue):
                search_1, search_2 = self.bfs1, self.bfs2
            else:
                search_1, search_2 = self.bfs2, self.bfs1

            current_cell = search_1.queue.pop(0)
            if search_2.visited[current_cell.x][current_cell.y]:
                return current_cell, search_2.visited[current_cell.x][current_cell.y]

            search_1.step(current_cell)


if __name__ == "__main__":
    n = 30
    src = Cell(0, 0)
    dest = Cell(29, 29)
    # road = BFS(n).run(src, dest)
    bs = BidirectionalSearch(n)
    road1, road2 = bs.run(src, dest)
    print(road1.dist, road2.dist)
