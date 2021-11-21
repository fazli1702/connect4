import random
import math
import sys
from termcolor import colored
from constant import *

def init_board():
    '''create board'''
    board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
    return board

def copy_board(board):
    new_board = []
    for row in board:
        new_row = []
        for col in row:
            new_row.append(col)
        new_board.append(new_row)
    return new_board

def print_board(board):
    '''print board nicely on terminal'''

    print()
    for row in board:
        new_row = []
        for col in range(COLS):
            if row[col] == PLAYER:
                new_row.append(colored('O', 'yellow'))
            elif row[col] == AI:
                new_row.append(colored('O', 'red'))
            else:
                new_row.append('.')
        print(' '.join(new_row))

    # print footer
    footer = ['-' for _ in range(COLS)]
    print('-'.join(footer))

    # print col number at bottom
    col_numbers = [str(i) for i in range(COLS)]
    print(' '.join(col_numbers))

    print()


def is_valid(board, col):
    '''check if col is not full'''
    if board[0][col] != EMPTY:  # check top most row
        return False
    return True


def get_valid_col(board):
    valid_col = []
    for col in range(COLS):
        if is_valid(board, col):
            valid_col.append(col)
    return valid_col


def get_next_row(board, col):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            return row


def drop(player, board, col):
    row = get_next_row(board, col)
    board[row][col] = player


def has_won(player, board):
    '''check if player has won the game'''

    # check if 4 in a row
    for row in board:
        for col in range(COLS - 3):
            flag = True
            for i in range(WIN_LENGTH):
                j = col + i
                if row[j] != player:
                    flag = False
            if flag:
                return True

    # check if 4 in a col
    for col in range(COLS):
        for row in range(ROWS - 3):
            flag = True
            for i in range(WIN_LENGTH):
                j = row + i
                if board[j][col] != player:
                    flag = False
            if flag:
                return True

    # check if 4 in downwards diagonal 
    for col in range(COLS - 3):
        for row in range(ROWS - 3):
            flag = True
            for i in range(WIN_LENGTH):
                j = row + i
                k = col + i
                if board[j][k] != player:
                    flag = False
            if flag:
                return True

    # check if 4 in upwards diagonal
    for col in range(COLS - 3):
        for row in range(ROWS-1, 2, -1):
            flag = True
            for i in range(WIN_LENGTH):
                j = row - i
                k = col + i
                if board[j][k] != player:
                    flag = False
            if flag:
                return True


def get_player_input(turn, board):
    valid_col = get_valid_col(board)
    while True:
        col = input(f'Player {turn} column number: ')
        if col.isdigit():
            if int(col) in valid_col:
                return int(col)
        print('Please enter a valid column number')


# ------------------- AI -------------------------- #

'''
minimax ai resources

medium aritcle
https://medium.com/analytics-vidhya/artificial-intelligence-at-play-connect-four-minimax-algorithm-explained-3b5fc32e4a4f

keith galli
https://github.com/KeithGalli/Connect4-Python/blob/master/connect4_with_ai.py
https://www.youtube.com/watch?v=MMLtza3CZFM

wikipedia
https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
'''


def get_random_move(board, player):
    '''generate random move -- for testing'''
    valid_cols = get_valid_col(board)
    col = random.choice(valid_cols)
    return col

def get_best_move(board, player):
    valid_cols = get_valid_col(board)
    best_score = -10000
    best_col = random.choice(valid_cols)
    scores = [0 for _ in range(COLS)]
    for col in valid_cols:
        temp_board = copy_board(board)
        drop(AI, temp_board, col)
        score = score_position(temp_board, player)
        print(f'col {col}: {score}')
        print()

        if score > 0:
            scores[col] = colored(str(score), 'green')
        else:
            scores[col] = colored(str(-score), 'red')

        if score > best_score:
            best_score = score
            best_col = col

    print_board(board)
    print(' '.join(scores))
    return best_col


def count_score(sub_board, player):
    '''calculate score base on pieces in sub board'''
    score = 0
    opp_player = PLAYER
    if player == opp_player:
        opp_player = AI

    # 4 in a row - has won
    if sub_board.count(player) == 4:
        score += 100
    
    # 3 in sub_board & 1 empry space
    elif sub_board.count(player) == 3 and sub_board.count(EMPTY) == 1:
        score += 5

    # 2 in sub_board & 2 empry space
    elif sub_board.count(player) == 2 and sub_board.count(EMPTY) == 2:
        score += 2

    # opponent has 3 in sub_board & 1 empry space
    if sub_board.count(opp_player) == 3 and sub_board.count(EMPTY) == 1:
        score -= 10

    return score
    


def score_position(board, player):
    '''split board into smaller sub board and evaluate the scores of the sub board'''
    score = 0

    # check center column (priotise center column)
    center_col_i = COLS // 2
    center_sub_col = [board[i][center_col_i] for i in range(ROWS)]
    delta_score = center_sub_col.count(player) * 5
    score += delta_score

    # check row
    for row in board:
        for col in range(COLS - 3):
            sub_row = row[col:col + WIN_LENGTH]
            delta_score = count_score(sub_row, player)
            score += delta_score
            

    # check col
    for col in range(COLS):
        for row in range(ROWS - 3):
            sub_col = [board[row+i][col] for i in range(WIN_LENGTH)]
            delta_score = count_score(sub_col, player)
            score += delta_score

    # check downwards diagonal
    for col in range(COLS - 3):
        for row in range(ROWS - 3):
            sub_down_diagonal = []
            for i in range(WIN_LENGTH):
                row_i = ROWS - WIN_LENGTH - row + i
                sub_down_diagonal.append(board[row_i][col+i])
            delta_score = count_score(sub_down_diagonal, player)
            score += delta_score

    # check upwards diagonal
    for col in range(COLS - 3):
        for row in range(ROWS-1, 2, -1):
            sub_up_diagonal = [board[row-i][col+i] for i in range(WIN_LENGTH)]
            delta_score = count_score(sub_up_diagonal, player)
            score += delta_score

    return score


def is_terminal_node(board):
    '''check if board in end state -- no more valid moves / player has won'''
    if len(get_valid_col(board)) == 0:
        return True
    if has_won(PLAYER, board):
        return True
    if has_won(AI, board):
        return True
    return False


def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_cols = get_valid_col(board)
    is_terminal = is_terminal_node(board)

    if depth == 0 or is_terminal:
        if is_terminal:
            # AI wins
            if has_won(AI, board):
                return None, 100000000

            # human wins
            elif has_won(PLAYER, board):
                return None, -100000000

            # no valid moves
            else:
                return None, 0

        # depth = 0
        else:
            return None, score_position(board, AI)

    # maximizing -- AI
    if maximizingPlayer:
        value = -math.inf
        curr_col = random.choice(valid_cols)
        for col in valid_cols:
            tmp_board = copy_board(board)
            drop(AI, tmp_board, col)

            score = minimax(tmp_board, depth-1, alpha, beta, False)[1]
            if score > value:
                value = score
                curr_col = col

            alpha = max(alpha, value)
            if alpha >= beta:
                break

        return curr_col, value

    # minimizing -- human player
    else:
        value = math.inf
        curr_col = random.choice(valid_cols)
        for col in valid_cols:
            tmp_board = copy_board(board)
            drop(PLAYER, tmp_board, col)

            score = minimax(tmp_board, depth-1, alpha, beta, True)[1]
            if score < value:
                value = score
                curr_col = col

            beta = min(beta, value)
            if alpha >= beta:
                break

        return curr_col, value



# --------------------- main ----------------------------- #

def play():
    board = init_board()
    print_board(board)
    turn = random.randint(0, 1)
    
    while True:
        if turn == 1:
            # player 1 turn
            p1 = get_player_input(1, board)
            drop(PLAYER, board, p1)
            print_board(board)

            # check if player 1 has won
            if has_won(PLAYER, board):
                print(colored('Player 1', 'yellow') + ' has won!!!')
                break

            turn -= 1

        else:
            # player 2 turn
            p2, minimax_score =  minimax(board, DEPTH, -math.inf, math.inf, True)
            drop(AI, board, p2)
            print(f'AI chose column {p2}')
            print_board(board)

            # check if player 2 has won
            if has_won(AI, board):
                print(colored('AI', 'red') + ' has won!!!')
                break

            turn += 1


def main():
    while True:
        play()
        while True:
            play_again = input('Play again? [y/n] ')
            if play_again.lower() == 'n':
                sys.exit(0)
            elif play_again.lower() == 'y':
                main()





if __name__ == '__main__':
    main()