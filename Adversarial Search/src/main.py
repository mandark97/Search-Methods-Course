class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_state = [['.', '.', '.'],
                              ['.', '.', '.'],
                              ['.', '.', '.']]

        # X plays first
        self.player_turn = 'X'

    def draw_board(self):
        for i in range(0, 3):
            print("|".join(self.current_state[i]))
        print()

    # check if player's move is valid
    def is_valid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        else:
            return self.current_state[px][py] == '.'

    # checks if the game has ended and returns the winner in each case
    def is_end(self):
        # vertical win
        for i in range(0, 3):
            if (self.current_state[0][i] != '.' and
                self.current_state[0][i] == self.current_state[1][i] and
                    self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i]

        # horizontal win
        for i in range(0, 3):
            if (self.current_state[i] == ['X', 'X', 'X']):
                return 'X'
            elif (self.current_state[i] == ['O', 'O', 'O']):
                return 'O'

        # main diagonal win
        if (self.current_state[0][0] != '.' and
            self.current_state[0][0] == self.current_state[1][1] and
                self.current_state[0][0] == self.current_state[2][2]):
            return self.current_state[0][0]

        # second diagonal win
        if (self.current_state[0][2] != '.' and
            self.current_state[0][2] == self.current_state[1][1] and
                self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]

        # full board?
        for i in range(0, 3):
            for j in range(0, 3):
                # check if cell is empty
                if (self.current_state[i][j] == '.'):
                    return None

        # tie
        return '.'

    def check_result(self, result):
        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

    def max(self):
        # Possible values for maxv are:
        # -1 - loss
        # 0  - a tie
        # 1  - win

        # We're initially setting it to -2 as worse than the worst case:
        maxv = -2

        px = None
        py = None

        result = self.check_result(self.is_end())
        if result != None:
            return result

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'O'
                    (m, _, _) = self.min()
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    # Setting back the field to empty
                    self.current_state[i][j] = '.'
        return (maxv, px, py)

    def min(self):
        # Possible values for minv are:
        # -1 - win
        # 0  - a tie
        # 1  - loss

        # We're initially setting it to 2 as worse than the worst case:
        minv = 2

        qx = None
        qy = None

        result = self.check_result(self.is_end())
        if result != None:
            return result

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'X'
                    (m, _, _) = self.max()
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.current_state[i][j] = '.'

        return (minv, qx, qy)

    def print_result(self):
        if self.result == 'X':
            print('The winner is X!')
        elif self.result == 'O':
            print('The winner is O!')
        elif self.result == '.':
            print("It's a tie!")

    def play(self, human_input=False):
        while True:
            self.draw_board()
            self.result = self.is_end()

            if self.result != None:
                self.print_result()
                self.initialize_game()
                return

            # If it's player's turn
            if self.player_turn == 'X':
                while True:
                    (_, qx, qy) = self.min()
                    print('Recommended move: X = {}, Y = {}'.format(qx, qy))

                    if human_input:
                        pmove = input(
                            "Inset X Y coordinates separated by space: ")
                        px, py = map(int, pmove.split(" "))
                    else:
                        (px, py) = (qx, qy)

                    if self.is_valid(px, py):
                        self.current_state[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print('The move is not valid! Try again.')
            # If it's AI's turn
            else:
                (m, px, py) = self.max()
                self.current_state[px][py] = 'O'
                self.player_turn = 'X'


def main():
    g = Game()
    g.play(human_input=False)


if __name__ == "__main__":
    main()
