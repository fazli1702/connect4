# window size
ROWS, COLS = 6, 7
SQUARE_SIZE = 120
HEIGHT, WIDTH = ROWS * SQUARE_SIZE, COLS * SQUARE_SIZE
RADIUS = (SQUARE_SIZE - 20) // 2  # radius of piece

DEPTH = 5 # minimax algorithm

# piece representation on board
PLAYER = 1
AI = 2
EMPTY = 0

WIN_LENGTH = 4 # length to win connect 4

# rgb colours
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)