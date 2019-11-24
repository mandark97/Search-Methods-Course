from random import choice
from collections import Counter
from random import randrange


class NQueensSearch(object):
    def __init__(self, N):
        self.N = N

    def initial(self):
        return [randrange(self.N) for i in range(self.N)]

    # number of pairs of queens atacking each other
    def heuristic(self, state):
        a, b, c = [Counter() for i in range(3)]

        for row, col in enumerate(state):
            a[col] += 1
            b[row - col] += 1
            c[row + col] += 1
        h = 0

        for count in [a, b, c]:
            for key in count:
                h += count[key] * (count[key] - 1) / 2
        return -h

    def near_states(self, state):
        near_states = []
        for row in range(self.N):
            for col in range(self.N):
                if col != state[row]:
                    aux = list(state)
                    aux[row] = col
                    near_states.append(list(aux))

        return near_states
