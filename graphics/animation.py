from maze.utils import colors, ANIMATION_DELAY, convert_grid_to_pixel, CELL_SIZE
from .draw import draw_maze, draw_start_and_end
import pygame

def generation_animation_step(window):
    window.fill(colors.BLACK)
    draw_maze(window)
    pygame.display.update()
    pygame.time.delay(ANIMATION_DELAY)

def solver_animation_step(window, color, gx, gy):
    px, py = convert_grid_to_pixel(gx, gy)
    pygame.draw.rect(window, color, (px, py, CELL_SIZE, CELL_SIZE))

    draw_maze(window)
    draw_start_and_end(window)

    pygame.display.update()
    pygame.time.delay(ANIMATION_DELAY)