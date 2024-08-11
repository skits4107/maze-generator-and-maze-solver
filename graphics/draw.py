import pygame

from maze.state import (maze_adjacency_list, 
                        end_pos, 
                        start_pos)
from maze.utils import (convert_grid_to_pixel, 
                        get_cell_center, 
                        CELL_SIZE, 
                        colors)


def draw_maze(window, draw_path=False):

    for cell in maze_adjacency_list:
        gx, gy = cell[0], cell[1]
        neighbors = maze_adjacency_list[(gx, gy)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for direction in directions:
            #draw a wall in directions that dont lead to neighbors
            if (gx + direction[0], gy + direction[1]) not in neighbors:

                start_px, start_py, end_px, end_py = 0, 0, 0, 0

                if direction[0] == -1:  #left
                    start_px, start_py = convert_grid_to_pixel(gx, gy)
                    end_px, end_py = convert_grid_to_pixel(gx, gy + 1)
                elif direction[0] == 1:  #right
                    start_px, start_py = convert_grid_to_pixel(gx + 1, gy)
                    end_px, end_py = convert_grid_to_pixel(gx + 1, gy + 1)
                elif direction[1] == -1:  #up
                    start_px, start_py = convert_grid_to_pixel(gx, gy)
                    end_px, end_py = convert_grid_to_pixel(gx + 1, gy)
                else:  #down
                    start_px, start_py = convert_grid_to_pixel(gx, gy + 1)
                    end_px, end_py = convert_grid_to_pixel(gx + 1, gy + 1)

                pygame.draw.line(window,
                                 colors.WHITE, (start_px, start_py), (end_px, end_py),
                                 width=2)

        if len(neighbors) == 0:
            break

        if draw_path:
            for neighbor in neighbors:
                if draw_path:
                    curr_px, curr_py = get_cell_center(gx, gy)
                    neighbor_px, neighbor_py = get_cell_center(
                        neighbor[0], neighbor[1])

                    pygame.draw.circle(window, colors.BLUE, (curr_px, curr_py), 3)
                    pygame.draw.line(window,
                                     colors.BLUE, (curr_px, curr_py),
                                     (neighbor_px, neighbor_py),
                                     width=2)
                    pygame.draw.circle(window, colors.BLUE,
                                       (neighbor_px, neighbor_py), 3)



def draw_path(path, color, window):
    for pos in path:
        px, py = convert_grid_to_pixel(pos[0], pos[1])
        pygame.draw.rect(window, color, (px, py, CELL_SIZE, CELL_SIZE))


def draw_start_and_end(window):
    start_px, start_py = get_cell_center(start_pos[0], start_pos[1])
    pygame.draw.circle(window, colors.GREEN, (start_px, start_py), 3)

    end_px, end_py = get_cell_center(end_pos[0], end_pos[1])
    pygame.draw.circle(window, colors.RED, (end_px, end_py), 3)
