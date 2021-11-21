import pygame
from constant import *
from game import Game
from connect4 import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('connect 4')

def main():
    run = True
    game = Game(WIN)
    print_board(game.get_board())

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # ai move
            if game.get_turn() == AI:
                game.ai_move()

            # mouse left click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_coordinate = pygame.mouse.get_pos()
                col = game.get_col_from_mouse_pos(mouse_coordinate)
                game.drop(col)

        game.update()

    pygame.quit()


if __name__ == '__main__':
    main()