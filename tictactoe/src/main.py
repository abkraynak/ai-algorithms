# main.py

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


class TicTacToe(object):
    def __init__(self, player1: str, player2: str):
        self.size = 3
        self.player1 = player1
        self.player2 = player2
        self.count1 = 0
        self.count2 = 0


    def minimax(self, board, computer: bool) -> int:
        self.count1 += 1
        score = board.check_if_win(self.player1, self.player2)
        if score == -1 or score == 1:
            return score
        if board.completed():
            return 0

        if computer:
            best = -10
            for i in range(self.size):
                for j in range(self.size):
                    if board.board[i][j] == '_':
                        board.board[i][j] = self.player2
                        best = max(best, self.minimax(board, not computer))
                        board.board[i][j] = '_'
            return best

        else:
            best = 10
            for i in range(self.size):
                for j in range(self.size):
                    if board.board[i][j] == '_':
                        board.board[i][j] = self.player1
                        best = min(best, self.minimax(board, not computer))
                        board.board[i][j] = '_'
            return best


    def next_move(self, board):
        best_value = -10
        for i in range(self.size):
            for j in range(self.size):
                if board.board[i][j] == '_':
                    board.board[i][j] = self.player2
                    value = self.minimax(board, False)
                    if value > best_value:
                        new_board = Board(board.board)
                        best_value = value
                    board.board[i][j] = '_'
        return new_board


    def alpha_beta_pruning(self, board, alpha: int, beta: int, computer: bool) -> int:
        self.count2 += 1
        score = board.check_if_win(self.player1, self.player2)
        if score == -1 or score == 1:
            return score
        if board.completed():
            return 0

        if computer:
            best = -10
            for i in range(self.size):
                for j in range(self.size):
                    if board.board[i][j] == '_':
                        board.board[i][j] = self.player2
                        best = max(best, self.alpha_beta_pruning(board, alpha, beta, not computer))
                        board.board[i][j] = '_'
                        alpha = max(alpha, best)
                        if beta <= alpha:
                            break
            return best

        else:
            best = 10
            for i in range(self.size):
                for j in range(self.size):
                    if board.board[i][j] == '_':
                        board.board[i][j] = self.player1
                        best = min(best, self.alpha_beta_pruning(board, alpha, beta, not computer))
                        board.board[i][j] = '_'
                        beta = min(beta, best)
                        if beta <= alpha:
                            break
            return best
    

    def next_move_alpha_beta(self, board, alpha: int, beta: int) -> int:
        best_value = -10
        for i in range(self.size):
            for j in range(self.size):
                if board.board[i][j] == '_':
                    board.board[i][j] = self.player2
                    value = self.alpha_beta_pruning(board, alpha, beta, False)
                    if value > best_value:
                        new_board = Board(board.board)
                        best_value = value
                    board.board[i][j] = '_'
        return new_board


if __name__ == '__main__':
    user = ''
    computer = ''
    turn = True
    pruning = False
    alpha = -10
    beta = 10

    while True:
        print('Choose your character (X or O):')
        inp = input()
        if inp == 'X':
            user = 'X'
            computer = 'O'
            print()
            break
        elif inp == 'O':
            user = 'O'
            computer = 'X'
            print()
            break
        else:
            print('Invalid character! Try again')
            print()
            continue

    while True:
        print('Use pruning? (Y=yes, N=no)')
        inp = input()
        if inp == 'Y':
            pruning = True
            print()
            break
        elif inp == 'N':
            print()
            break
        else:
            print('Invalid character! Try again')
            print()
            continue

    b = Board(None)
    t = TicTacToe(user, computer)

    for i in range(9):
        if turn:
            while True:
                print('Your turn . . .')
                x = int(input('row = ')) - 1
                if x > 2 or x < 0:
                    print('Invalid value for row! Try again')
                    print()
                    continue

                y = int(input('col = ')) - 1
                if y > 2 or y < 0:
                    print('Invalid value for column! Try again')
                    print()
                    continue

                if b.board[x][y] != '_':
                    print('Invalid move! Try again')
                    print()
                    continue

                b.board[x][y] = user
                print()
                b.print()
                turn = False
                print()
                break

        else:
            print('Computer\'s turn . . .')
            if pruning:
                b = t.next_move_alpha_beta(b, alpha, beta)
                print()
                b.print()
                turn = True
                print()

            else:
                b = t.next_move(b)
                print()
                b.print()
                turn = True
                print()
        
        print()
        if b.check_if_win(user, computer) == -1:
            print('You win!')
            break
        elif b.check_if_win(user, computer) == 1:
            print('You lost!')
            break
        if b.completed == True:
            print('It\'s a tie!')
            break
        
    print()
    if pruning:
        print('Iterations:', t.count2)
    else:
        print('Iterations:', t.count1)