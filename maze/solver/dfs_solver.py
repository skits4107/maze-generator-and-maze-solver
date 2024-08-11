from maze.utils import calc_distance, colors
from maze.state import (end_pos, maze_adjacency_list, start_pos)
from graphics.animation import solver_animation_step

def dfs_solve(window):
    visited = []
    path = []
    _dfs_solver(start_pos[0], start_pos[1], visited, path, window)
    return visited, path


def _dfs_solver(gx, gy, visited, path, window):
    #base cases
    if (gx, gy) in visited:
        return False
    if (gx, gy) == end_pos:
        path.append((gx, gy))
        return True
    neighbors = maze_adjacency_list[(gx, gy)]
    if len(neighbors) == 0:
        return False

    #mark visted and path
    visited.append((gx, gy))
    path.append((gx, gy))

    #draw path
    solver_animation_step(window, colors.PURPLE, gx, gy)

    #recursive cals to neighboring cells
    neighbors.sort(key=lambda posA, posB=end_pos: calc_distance(posA, posB))
    for neighbor in neighbors:
        if _dfs_solver(neighbor[0], neighbor[1], visited, path, window):
            return True

    #this wasnt part fo the path
    path.remove((gx, gy))

    #draw visted sqaures
    solver_animation_step(window, colors.DARK_PURPLE, gx, gy)

    #return false as their was not successful path form this node
    return False