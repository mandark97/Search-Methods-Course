from n_queens import NQueensSearch


def printBoard(result, state=""):
    board = []
    for col in result:
        line = ['.'] * len(result)
        line[col] = 'Q'
        board.append(' '.join(line))
    print(state)
    print("\n".join(board))


def hill_climbing(problem):
    current = problem.initial()
    printBoard(current, state="initial")
    step = 0
    while True:
        step = step + 1
        neighbors = problem.near_states(current)
        if not neighbors:
            break
        neighbor = max(neighbors, key=lambda state: problem.heuristic(state))
        if problem.heuristic(neighbor) <= problem.heuristic(current):
            break
        current = neighbor
        printBoard(current, state=f"step {step}")
    return current


if __name__ == "__main__":
    problem = NQueensSearch(8)
    result = hill_climbing(problem)
    printBoard(result, state="final")
