import random
import sys
import math
import pygame
from constant import *
from connect4 import *

class Game:
    def __init__(self, win):
        self.board = init_board()
        self.turn = random.choice([PLAYER, AI])
        self.win = win  # pygame window

    def get_turn(self):
        return self.turn

    def get_board(self):
        return self.board

    def get_col_from_mouse_pos(self, pos):
        x, y = pos
        col = x // SQUARE_SIZE
        return col

    def drop(self, col):
        valid_cols = get_valid_col(self.board)
        if col in valid_cols:
            drop(self.turn, self.board, col)
            print_board(self.board)

            if has_won(self.turn, self.board):
                if self.turn == AI:
                    win_player = colored('AI', 'red')
                else:
                    win_player = colored('Player', 'yellow')

                print(win_player, 'has won!!!')
                sys.exit(0)

            self.update_next_turn()

    def ai_move(self):
        ai_col, points = minimax(self.board, DEPTH, -math.inf, math.inf, True)
        return ai_col

    def update_next_turn(self):
        if self.turn == AI:
            self.turn = PLAYER
        else:
            self.turn = AI

    def update(self):
        self.draw_board()
        pygame.display.update()

    def draw_board(self):
        for row in range(ROWS):
            for col in range(COLS):

                # draw blue boxes
                pygame.draw.rect(self.win, BLUE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

                # draw black circle / piece in blue box
                x = ((col + 1) * SQUARE_SIZE) - (SQUARE_SIZE // 2)
                y = ((row + 1) * SQUARE_SIZE) - (SQUARE_SIZE // 2)
                center = (x, y)
                if self.board[row][col] == PLAYER:
                    pygame.draw.circle(self.win, YELLOW, center, RADIUS)
                elif self.board[row][col] == AI:
                    pygame.draw.circle(self.win, RED, center, RADIUS)
                else:
                    pygame.draw.circle(self.win, BLACK, center, RADIUS)

