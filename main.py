import pygame, sys
import random
import math
#global variables and constants


# use this line if you want bigger mazes: sys.setrecursionlimit(new_limit)
# default limit is 1000.
# please note that increasing the recursion limit too much can potenitally cause stack overflow errors
grid_width = 30
grid_height = 30
cell_size = 10

width = (grid_width + 2) * cell_size
height = (grid_height + 2) * cell_size

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
DARK_PURPLE = (100, 0, 100)

maze_adjacency_list = {}

start_pos = (5, 0)
end_pos = (grid_width, grid_height)

animation_delay = 50


#returns pixel coordinates of top left corner
def convert_grid_to_pixel(gx, gy):
    px = gx * cell_size
    py = gy * cell_size
    return px, py


def get_cell_center(gx, gy):
    cx, cy = convert_grid_to_pixel(gx, gy)
    cx, cy = cx + cell_size / 2, cy + cell_size / 2
    return cx, cy


def dfs_maze_generator(gx, gy, prev_x, prev_y, window):
    #makesure we do not go out of bounds
    if gx < 0 or gx > grid_width or gy < 0 or gy > grid_height:
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
    window.fill(BLACK)
    draw_maze(window)
    pygame.display.update()
    pygame.time.delay(animation_delay)
    #keep exploring random direcitons until you explore all of them.
    while len(possible_neighbors) > 0:
        choice = random.choice(possible_neighbors)
        possible_neighbors.remove(choice)

        #add choice to neighbor list assuming it is valid before recursing to it
        maze_adjacency_list[(gx, gy)].append(choice)

        #if it wasnt valid, remove it
        if not dfs_maze_generator(choice[0], choice[1], gx, gy, window):
            maze_adjacency_list[(gx, gy)].remove(choice)

    #after exploring all neighbors randomly we back trakc and return true to
    #in order to add it as neighbor the previous node/tile
    return True


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
                                 WHITE, (start_px, start_py), (end_px, end_py),
                                 width=2)

        if len(neighbors) == 0:
            break

        if draw_path:
            for neighbor in neighbors:
                if draw_path:
                    curr_px, curr_py = get_cell_center(gx, gy)
                    neighbor_px, neighbor_py = get_cell_center(
                        neighbor[0], neighbor[1])

                    pygame.draw.circle(window, BLUE, (curr_px, curr_py), 3)
                    pygame.draw.line(window,
                                     BLUE, (curr_px, curr_py),
                                     (neighbor_px, neighbor_py),
                                     width=2)
                    pygame.draw.circle(window, BLUE,
                                       (neighbor_px, neighbor_py), 3)

        #draw_maze(window, neighbor[0], neighbor[1], previously_drawn, draw_path=draw_path)


#sets the end position by finding all dead ends and selecting randomly
# i do not know if this is the most effecient way but it works
def set_end_point():
    global end_pos
    end_points = []
    for pos in maze_adjacency_list:
        if len(maze_adjacency_list[pos]) == 1 and pos != start_pos:
            end_points.append(pos)
    end_pos = random.choice(end_points)


def calc_distance_to_end(posA):
    return math.sqrt((posA[0] - end_pos[0])**2 + (posA[1] - end_pos[1])**2)


def dfs_solver(gx, gy, visited, path, window):
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
    px, py = convert_grid_to_pixel(gx, gy)
    pygame.draw.rect(window, PURPLE, (px, py, cell_size, cell_size))

    draw_maze(window)
    draw_start_and_end(window)

    pygame.display.update()
    pygame.time.delay(animation_delay)

    #recursive cals to neighboring cells
    neighbors.sort(key=calc_distance_to_end)
    for neighbor in neighbors:
        if dfs_solver(neighbor[0], neighbor[1], visited, path, window):
            return True

    #this wasnt part fo the path
    path.remove((gx, gy))

    #draw visted sqaures
    pygame.draw.rect(window, DARK_PURPLE, (px, py, cell_size, cell_size))

    draw_maze(window)
    draw_start_and_end(window)

    pygame.display.update()
    pygame.time.delay(animation_delay)

    #return false as their was not successful path form this node
    return False


def draw_path(path, color, window):
    for pos in path:
        px, py = convert_grid_to_pixel(pos[0], pos[1])
        pygame.draw.rect(window, color, (px, py, cell_size, cell_size))


def draw_start_and_end(window):
    start_px, start_py = get_cell_center(start_pos[0], start_pos[1])
    pygame.draw.circle(window, GREEN, (start_px, start_py), 3)

    end_px, end_py = get_cell_center(end_pos[0], end_pos[1])
    pygame.draw.circle(window, RED, (end_px, end_py), 3)


def check_recursion_limit():
    # the theoritical maximim amount the algorithm might recurse is effectively the area of the grid
    # Note: it is unlikely for it to actually reach the maximum depth due to back tracking and randomness
    return (grid_height*grid_width < sys.getrecursionlimit())
        

def main():
    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Hello World!')

    if check_recursion_limit():
        print("Warning: maze dimensions may go over recursion limit")

    dfs_maze_generator(start_pos[0], start_pos[1], start_pos[0], start_pos[1],
                       window)
    set_end_point()
    draw_start_and_end(window)
    visited = []
    path = []
    dfs_solver(start_pos[0], start_pos[1], visited, path, window)
    print(path)
    while True:
        window.fill(BLACK)

        draw_path(visited, DARK_PURPLE, window)
        draw_path(path, PURPLE, window)
        draw_start_and_end(window)

        draw_maze(window, False)
        pygame.display.update()


if __name__ == "__main__":
    main()
