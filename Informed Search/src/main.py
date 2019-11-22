class Node(object):
    def __init__(self, parent, position):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, cell):
        return self.position == cell.position

    def move(self, movement):
        return Node(self, (self.position[0] + movement[0], self.position[1] + movement[1]))

    def is_valid(self, maze):
        if self.position[0] > (len(maze) - 1) or \
                self.position[0] < 0 or \
                self.position[1] > (len(maze[len(maze) - 1]) - 1) or \
                self.position[1] < 0 or \
                maze[self.position[0]][self.position[1]] != 0:
            return False

MOVEMENTS = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
def astar(maze, start, end):
    start_node = Node(None, start)
    end_node = Node(None, end)

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while(len(open_list) > 0):

        current_node = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent

            return path[::-1]

        children = []

        # Adjacent squares
        for new_position in MOVEMENTS:
            new_node = current_node.move(new_position)

            if new_node.is_valid(maze):
                children.append(new_node)

        for child in children:
            if child in closed_list:
                continue

            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) **
                       2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            open_list.append(child)
