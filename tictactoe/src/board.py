# board.py

class Board(object):
    def __init__(self, board):
        self.size = 3
        if board == None:
            self.board = [
                ['_', '_', '_'],
                ['_', '_', '_'],
                ['_', '_', '_']
            ]
        else:
            b = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
            for i in range(self.size):
                for j in range(self.size):
                    b[i][j] = board[i][j]
            self.board = b


    def print(self):
        space = ' '
        for i in range(self.size):
            for j in range(self.size):
                if j < self.size - 1:
                    print(space + self.board[i][j], end = ' |')
                else:
                    print(space + self.board[i][j])
            if i < self.size - 1:
                print('--- --- ---')


    def completed(self) -> bool:
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == '_':
                    return False
        return True


    def check_if_win(self, player1: str, player2: str) -> int:
        # Horizontals
        for i in range(self.size):
            if self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                if self.board[i][0] == player1:
                    return -1
                elif self.board[i][0] == player2:
                    return 1
                
        # Verticals
        for i in range(self.size):
            if self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                if self.board[0][i] == player1:
                    return -1
                elif self.board[0][i] == player2:
                    return 1

        # Diagonals
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            if self.board[0][0] == player1:
                return -1
            elif self.board[0][0] == player2:
                return 1
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            if self.board[0][2] == player1:
                return -1
            elif self.board[0][2] == player2:
                return 1

        return 0