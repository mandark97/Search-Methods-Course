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

    # check if is in maze's boundries and is not a wall
    def is_valid(self, maze):
        return self.position[0] < len(maze) and \
            self.position[0] >= 0 and \
            self.position[1] < len(maze[0]) and \
            self.position[1] >= 0 and \
            maze[self.position[0]][self.position[1]] == 0


MOVEMENTS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
# MOVEMENTS = [(0, -1), (0, 1), (-1, 0), (1, 0),
#              (-1, -1), (-1, 1), (1, -1), (1, 1)]


class InformedSearch(object):
    def __init__(self, maze, start, end):
        if maze[start[0]][start[1]] == 1:
            raise "Invalid start"

        if maze[end[0]][end[1]] == 1:
            raise "Invalid end"

        self.start_node = Node(None, start)
        self.end_node = Node(None, end)
        self.maze = maze

    def run(self, mode="greedy"):
        open_list = []
        closed_list = []
        open_list.append(self.start_node)

        while(len(open_list) > 0):
            current_node, current_index = self.__select_current_node(open_list)
            open_list.pop(current_index)
            closed_list.append(current_node)

            if current_node == self.end_node:
                return self.__return_path(current_node)

            for child in self.__compute_children(current_node):
                if child in closed_list:
                    continue

                if mode == "greedy":
                    self.__greedy_update(child, current_node)
                elif mode == "a_star":
                    self.__a_star_update(child, current_node)

                if any([child == open_node and child.g > open_node.g for open_node in open_list]):
                    continue

                open_list.append(child)

    def __greedy_update(self, child, current_node):
        child.g = current_node.g + 1
        child.h = self.__compute_h(child, self.end_node)
        child.f = child.h

    def __a_star_update(self, child, current_node):
        child.g = current_node.g + 1
        child.h = self.__compute_h(child, self.end_node)
        child.f = child.g + child.h

    def __return_path(self, node):
        path = []
        while node is not None:
            path.append(node.position)
            node = node.parent

        return path[::-1]

    def __select_current_node(self, open_list):
        current_node = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        return current_node, current_index

    def __compute_h(self, node, end_node):
        return ((node.position[0] - end_node.position[0]) ** 2) + ((node.position[1] - end_node.position[1]) ** 2)

    def __compute_children(self, current_node):
        children = []

        # Adjacent squares
        for new_position in MOVEMENTS:
            new_node = current_node.move(new_position)

            if new_node.is_valid(self.maze):
                children.append(new_node)

        return children


def main():
    maze = [[0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)

    path = InformedSearch(maze, start, end).run(mode="a_star")
    print(path)


if __name__ == '__main__':
    main()
