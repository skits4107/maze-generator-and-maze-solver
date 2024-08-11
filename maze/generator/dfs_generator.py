from maze.utils import GRID_WIDTH, GRID_HEIGHT
from maze.state import maze_adjacency_list, start_pos
from graphics.animation import generation_animation_step
import random


def dfs_generate(window):
    _dfs_generate(start_pos[0], start_pos[1], start_pos[0], start_pos[1], window)
    


def _dfs_generate(gx, gy, prev_x, prev_y, window):
    #makesure we do not go out of bounds
    if gx < 0 or gx > GRID_WIDTH or gy < 0 or gy > GRID_HEIGHT:
        return False
    #do not wantto vist an already visted node/tile
    if (gx, gy) in maze_adjacency_list:
        return False

    #all possible direcitons for exploration
    possible_neighbors = [(gx + 1, gy), (gx - 1, gy), (gx, gy + 1),
                          (gx, gy - 1)]

    #add current node to adjecency list to mark as visited and set one of its neigbors
    #to the previous node
    maze_adjacency_list[(gx, gy)] = [(prev_x, prev_y)]

    #draw maze in real time
    generation_animation_step(window)

    #keep exploring random direcitons until you explore all of them.
    while len(possible_neighbors) > 0:
        choice = random.choice(possible_neighbors)
        possible_neighbors.remove(choice)

        #add choice to neighbor list assuming it is valid before recursing to it
        maze_adjacency_list[(gx, gy)].append(choice)

        #if it wasnt valid, remove it
        if not _dfs_generate(choice[0], choice[1], gx, gy, window):
            maze_adjacency_list[(gx, gy)].remove(choice)

    #after exploring all neighbors randomly we back trakc and return true to
    #in order to add it as neighbor the previous node/tile
    return True
