#global variables and constants


# use this line if you want bigger mazes: sys.setrecursionlimit(new_limit)
# default limit is 1000.
# please note that increasing the recursion limit too much can potenitally cause stack overflow errors
GRID_WIDTH = 30
GRID_HEIGHT = 30
CELL_SIZE = 10

DISPLAY_WIDTH = (GRID_WIDTH + 2) * CELL_SIZE
DISPLAY_HEIGHT = (GRID_HEIGHT + 2) * CELL_SIZE

class colors:
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    PURPLE = (255, 0, 255)
    DARK_PURPLE = (100, 0, 100)

ANIMATION_DELAY = 10

