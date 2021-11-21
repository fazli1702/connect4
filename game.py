import random
from sys import displayhook
import time
import math
import pygame
from constant import *
from connect4 import *

class Game:
    def __init__(self, win):
        self.board = init_board()
        self.turn = random.choice([PLAYER, AI])
        self.win = win  # pygame window
        self.winner = False  # check if there is a winner
        self.tie = False   # check if tie

    def get_turn(self):
        return self.turn

    def get_board(self):
        return self.board

    def get_winner(self):
        return self.winner

    def get_tie(self):
        return self.tie

    def get_col_from_mouse_pos(self, pos):
        '''get board column from mouse coordinate'''
        x, y = pos
        col = x // SQUARE_SIZE
        return col

    def ai_move(self):
        '''drop ai piece using minimax algorithm'''
        ai_col, points = minimax(self.board, DEPTH, -math.inf, math.inf, True)
        self.drop(ai_col)

    def update_next_turn(self):
        if self.turn == AI:
            self.turn = PLAYER
        else:
            self.turn = AI

    def update(self):
        '''update pygame window'''
        self.draw_board()
        if self.winner:
            self.display_winner(self.turn)
        if self.tie:
            self.display_tie()
        pygame.display.update()

    def reset(self):
        '''reset board to original state - restart game'''
        self.board = init_board()
        self.turn = random.choice([PLAYER, AI])
        self.winner = False

    def drop(self, col):
        valid_cols = get_valid_col(self.board)
        if col in valid_cols:
            drop(self.turn, self.board, col)
            if self.turn == AI:
                print(colored('AI', 'red'), 'col', col)
            else:
                print(colored('Player', 'yellow'), 'col', col)
            print_board(self.board)


    # https://stackoverflow.com/questions/23982907/how-to-center-text-in-pygame
    def display_winner(self, winner):
        # draw black rect in middle of window
        font_size = 100
        delta = font_size // 2
        h = 100
        mid_y = (HEIGHT // 2) - delta
        pygame.draw.rect(self.win, BLACK, (0, mid_y, WIDTH, h))

        # display text of winner on window
        pygame.font.init()
        font = pygame.font.Font(None, font_size)
        if winner == AI:
            text = font.render('AI has won!!!', True, RED)
        else:
            text = font.render('Player has won!!!', True, YELLOW)

        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        self.win.blit(text, text_rect)

    def display_tie(self):
        # draw black rect in middle of window
        font_size = 100
        delta = font_size // 2
        h = 100
        mid_y = (HEIGHT // 2) - delta
        pygame.draw.rect(self.win, BLACK, (0, mid_y, WIDTH, h))

        # display text of winner on window
        pygame.font.init()
        font = pygame.font.Font(None, font_size)
        text = font.render('Draw', True, WHITE)
        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        self.win.blit(text, text_rect)


    def check_win(self):
        '''check if there is a winner on board, display winner if there is'''
        if has_won(self.turn, self.board):
            self.winner = True
        else:
            self.update_next_turn()

    def check_tie(self):
        '''check if there is tie - no more valid col & no winner'''
        valid_cols = get_valid_col(self.board)
        if valid_cols == []:
            self.tie = True



    def draw_board(self):
        '''display board on pygame window'''
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

