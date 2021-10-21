# tictactoe.py 

from board import Board

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