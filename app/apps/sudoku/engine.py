import random
import copy
import time


class Sudoku:

    def __init__(self, board=None):
        self.numbers = list(range(1, 10))
        random.shuffle(self.numbers)

        if board == None:
            self.board = [['' for _ in range(9)] for _ in range(9)]
            self.solve()
            self.generated_board = copy.deepcopy(self.board)
        else:
            self.board = [[int(x) if x != '' else '' for x in row] for row in board]

    def get_board(self):
        return self.board

    def playable_board(self, difficulty):
        if difficulty == 'easy':
            i = 35
        elif difficulty == 'medium':
            i = 48
        elif difficulty == 'hard':
            i = 55
        while i > 0:
            y = random.randint(0, 8)
            x = random.randint(0, 8)
            if self.board[y][x] != '':
                self.generated_board[y][x] = ''
                i -= 1
            else:
                continue
        return self.generated_board

    def check_number(self, number, x, y):
        # row
        if number in self.board[y]:
            return False
        # column
        if number in [self.board[i][x] for i in range(9)]:
            return False
        # box
        yborder = y // 3
        xborder = x // 3
        for i in range(yborder*3, (yborder*3) + 3):
            if number in self.board[i][xborder * 3:xborder * 3 + 3]:
                return False
        return True

    def get_empty_cell(self, y, x):
        if x == 9:
            y += 1
            x = 0
        if y == 9 or self.board[y][x] == '':
            return y, x
        return self.get_empty_cell(y, x+1)

    def solve(self, x=0, y=0):
        # self.show()
        # time.sleep(0.1)

        y, x = self.get_empty_cell(y, x)
        if y == 9:
            return True

        for number in self.numbers:
            if self.check_number(number, x, y):
                self.board[y][x] = number
                if self.solve(x+1, y):
                    return True
            self.board[y][x] = ''

    def show(self):
        print('\n'.join(['|'.join([str(x) for x in row])
                         for row in self.board]))
        print('-' * 50)

    def check_cell(self, value, y, x):
        if self.board[y][x] == int(value):
            return True
        return False

# s = Sudoku()
