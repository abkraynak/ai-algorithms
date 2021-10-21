# main.py

from board import Board
from tictactoe import TicTacToe

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