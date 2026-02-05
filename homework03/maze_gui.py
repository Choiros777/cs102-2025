"""
code for drawing the labyrinth

"""

import tkinter as tk
from copy import deepcopy
from tkinter import ttk
from typing import List

from homework03.maze import add_path_to_grid, bin_tree_maze, solve_maze

GRID = None
CELL_SIZE = 10
canvas = None


def draw_cell(x, y, color, size: int = 10):
    """draws one cell of the labyrinth"""
    x *= size
    y *= size
    x1 = x + size
    y1 = y + size
    if canvas is None:
        raise ValueError("Canvas not initialized")
    canvas.create_rectangle(x, y, x1, y1, fill=color)


def draw_maze(grid: List[List[str | int]], size: int = 10):
    """i changed the colour to blue"""
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == " ":
                color = "White"
            elif cell == "■":
                color = "black"
            elif cell == "X":
                color = "blue"
            draw_cell(y, x, color, size)


def show_solution():
    """the else clause isnt needed because there will always be a solution"""
    maze, path = solve_maze(GRID)
    maze = add_path_to_grid(GRID, path)

    if path:
        draw_maze(maze, CELL_SIZE)


if __name__ == "__main__":
    N, M = 51, 77

    CELL_SIZE = 10
    GRID = bin_tree_maze(N, M)

    MAZE_IS_VALID = False
    while not MAZE_IS_VALID:
        current_maze = bin_tree_maze(N, M)
        _, solution_path = solve_maze(deepcopy(current_maze))
        if solution_path is not None:
            MAZE_IS_VALID = True
            GRID = current_maze

    window = tk.Tk()
    window.title("Maze")
    window.geometry("%dx%d" % (M * CELL_SIZE + 100, N * CELL_SIZE + 100))

    canvas = tk.Canvas(window, width=M * CELL_SIZE, height=N * CELL_SIZE)
    canvas.pack()

    draw_maze(GRID, CELL_SIZE)
    ttk.Button(window, text="Solve", command=show_solution).pack(pady=20)

    window.mainloop()
