from .constants import CELL_SIZE, GRID_HEIGHT, GRID_WIDTH
import math
import sys
import random

#returns pixel coordinates of top left corner
def convert_grid_to_pixel(gx, gy):
    px = gx * CELL_SIZE
    py = gy * CELL_SIZE
    return px, py


def get_cell_center(gx, gy):
    cx, cy = convert_grid_to_pixel(gx, gy)
    cx, cy = cx + CELL_SIZE / 2, cy + CELL_SIZE / 2
    return cx, cy

def calc_distance(posA, posB):
    return math.sqrt((posA[0] - posB[0])**2 + (posA[1] - posB[1])**2)

def check_recursion_limit():
    # the theoritical maximim amount the algorithm might recurse is effectively the area of the grid
    # Note: it is unlikely for it to actually reach the maximum depth due to back tracking and randomness
    return (GRID_HEIGHT*GRID_WIDTH < sys.getrecursionlimit())

