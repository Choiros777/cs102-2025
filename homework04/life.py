import pathlib
import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:

        rows_count = self.rows
        cols_count = self.cols

        result = []

        for _ in range(rows_count):
            if randomize:
                line = [random.randint(0, 1) for _ in range(cols_count)]
            else:
                line = [0 for _ in range(cols_count)]
            result.append(line)

        return result

    def get_neighbours(self, cell: Cell) -> Cells:
        # Copy from previous assignment
        row, col = cell
        neighbours = []

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue

                new_row, new_col = row + dr, col + dc

                if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                    neighbours.append(self.curr_generation[new_row][new_col])

        return neighbours

    def get_next_generation(self) -> Grid:
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        for row in range(self.rows):
            for col in range(self.cols):
                neighbours = self.get_neighbours((row, col))
                live_neighbours = sum(neighbours)

                current_cell = self.curr_generation[row][col]

                if current_cell == 1:
                    if live_neighbours in [2, 3]:
                        new_grid[row][col] = 1
                    else:
                        new_grid[row][col] = 0
                else:
                    if live_neighbours == 3:
                        new_grid[row][col] = 1
                    else:
                        new_grid[row][col] = 0

        return new_grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """

        self.prev_generation = [row[:] for row in self.curr_generation]
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        if self.max_generations is None:
            return False  # Unlimited generations, never exceeded
        return self.generations >= self.max_generations


    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        return self.curr_generation != self.prev_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """

        with open(filename, "r") as f:
            lines = f.readlines()

        rows = len(lines)
        cols = len(lines[0].strip()) if lines else 0

        game = GameOfLife((rows, cols), randomize=False, max_generations=float("inf"))

        grid = []
        for line in lines:
            row = [int(char) for char in line.strip()]
            grid.append(row)

        game.curr_generation = grid
        game.prev_generation = [[0] * cols for _ in range(rows)]

        return game

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename, "w") as f:
            for row in self.curr_generation:
                line = "".join(str(cell) for cell in row)
                f.write(line + "\n")
