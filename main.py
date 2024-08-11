import pygame
import random
from graphics import *
from maze.utils import DISPLAY_WIDTH, DISPLAY_HEIGHT, check_recursion_limit, colors
from maze.state import set_end_point
from maze.solver import dfs_solve
from maze.generator import dfs_generate
import sys
from pygame.locals import QUIT

def main():
    pygame.init()
    window = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption('Hello World!')

    if check_recursion_limit():
        print("Warning: maze dimensions may go over recursion limit")

    dfs_generate(window)
    set_end_point()
    draw_start_and_end(window)
    
    visited, path = dfs_solve(window)

    #print(path)

    clock = pygame.time.Clock()
    while True:
        window.fill(colors.BLACK)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        draw_path(visited, colors.DARK_PURPLE, window)
        draw_path(path, colors.PURPLE, window)
        draw_start_and_end(window)

        draw_maze(window, False)

        clock.tick(60)
        pygame.display.update()


if __name__ == "__main__":
    main()
