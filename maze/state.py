from .utils.constants import GRID_WIDTH, GRID_HEIGHT
import random

maze_adjacency_list = {}
start_pos = (0, 0)
end_pos = (GRID_WIDTH, GRID_HEIGHT)

def set_end_point():
    global end_pos
    end_points = []
    for pos in maze_adjacency_list:
        if len(maze_adjacency_list[pos]) == 1 and pos != start_pos:
            end_points.append(pos)
    end_pos = random.choice(end_points)