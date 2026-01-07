from copy import deepcopy
from random import choice, randint
from typing import List, Optional, Tuple, Union

import pandas as pd


def create_grid(rows: int = 15, cols: int = 15) -> List[List[Union[str, int]]]:
    return [["■"] * cols for _ in range(rows)]


def remove_wall(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> List[List[Union[str, int]]]:
    """
    :param grid:
    :param coord:
    :return:
    """

    row, col = coord
    last_col_index = len(grid[0]) - 1
    selected_direction = choice(["up", "right"])
    if selected_direction == "up":
        can_go_up = row > 1
        if can_go_up:
            grid[row - 1][col] = " "
        else:
            can_go_right = col < last_col_index - 1
            if can_go_right:
                grid[row][col + 1] = " "
    else:  # direction == "right"
        can_go_right = col < last_col_index - 1
        if can_go_right:
            grid[row][col + 1] = " "
        else:
            can_go_up = row > 1
            if can_go_up:
                grid[row - 1][col] = " "
    return grid


def bin_tree_maze(rows: int = 15, cols: int = 15, random_exit: bool = True) -> List[List[Union[str, int]]]:
    """

    :param rows:
    :param cols:
    :param random_exit:
    :return:
    """
    grid = create_grid(rows, cols)
    empty_cells = []
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if x % 2 == 1 and y % 2 == 1:
                grid[x][y] = " "
                empty_cells.append((x, y))

    # 1. выбрать любую клетку
    # 2. выбрать направление: наверх или направо.
    # Если в выбранном направлении следующая клетка лежит за границами поля,
    # выбрать второе возможное направление
    # 3. перейти в следующую клетку, сносим между клетками стену
    # 4. повторять 2-3 до тех пор, пока не будут пройдены все клетки

    for current_cell in empty_cells:
        remove_wall(grid, current_cell)
    # генерация входа и выхода
    if random_exit:
        x_in, x_out = randint(0, rows - 1), randint(0, rows - 1)
        y_in = randint(0, cols - 1) if x_in in (0, rows - 1) else choice((0, cols - 1))
        y_out = randint(0, cols - 1) if x_out in (0, rows - 1) else choice((0, cols - 1))
    else:
        x_in, y_in = 0, cols - 2
        x_out, y_out = rows - 1, 1
    grid[x_in][y_in], grid[x_out][y_out] = "X", "X"
    return grid


def get_exits(grid: List[List[Union[str, int]]]) -> List[Tuple[int, int]]:
    """

    :param grid:
    :return:
    """
    exits = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "X":
                exits.append((i, j))
    return exits


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param k:
    :return:
    """
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == k:

                if i > 0 and grid[i - 1][j] == 0:
                    grid[i - 1][j] = k + 1
                if i < rows - 1 and grid[i + 1][j] == 0:
                    grid[i + 1][j] = k + 1
                if j > 0 and grid[i][j - 1] == 0:
                    grid[i][j - 1] = k + 1
                if j < cols - 1 and grid[i][j + 1] == 0:
                    grid[i][j + 1] = k + 1
    return grid


def shortest_path(
    grid: List[List[Union[str, int]]], exit_coord: Tuple[int, int]
) -> Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]:
    """

    :param grid:
    :param exit_coord:
    :return:
    """

    current_x, current_y = exit_coord
    current_value = grid[current_x][current_y]

    if isinstance(current_value, str):
        try:
            current_value = int(current_value)
        except ValueError:
            return None

    if current_value == 1:
        return [exit_coord]

    path = [exit_coord]

    while current_value > 1:
        neighbor_found = False

        for direction_x, direction_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor_x = current_x + direction_x
            neighbor_y = current_y + direction_y

            if 0 <= neighbor_x < len(grid) and 0 <= neighbor_y < len(grid[0]):
                neighbor_value = grid[neighbor_x][neighbor_y]

                if isinstance(neighbor_value, str):
                    try:
                        neighbor_value = int(neighbor_value)
                    except ValueError:
                        continue

                if neighbor_value == current_value - 1:
                    path.append((neighbor_x, neighbor_y))
                    current_x, current_y = neighbor_x, neighbor_y
                    current_value -= 1
                    neighbor_found = True
                    break

        if not neighbor_found:
            return None

    return path


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """

    :param grid:
    :param coord:
    :return:
    """

    rows = len(grid)
    cols = len(grid[0])
    y, x = coord

    corner_positions = [(0, 0), (0, cols - 1), (rows - 1, 0), (rows - 1, cols - 1)]
    if (y, x) in corner_positions:
        return True

    if y == 0:
        if grid[y + 1][x] != " ":
            return True
    elif x == cols - 1:
        if grid[y][x - 1] != " ":
            return True
    elif y == rows - 1:
        if grid[y - 1][x] != " ":
            return True
    elif x == 0:
        if grid[y][x + 1] != " ":
            return True

    return False


def solve_maze(
    grid: List[List[Union[str, int]]],
) -> Tuple[List[List[Union[str, int]]], Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]]:
    """

    :param grid:
    :return:
    """
    grid = deepcopy(grid)
    exits = get_exits(grid)
    if len(exits) == 1:
        return grid, exits[0]
    for possible_exit in exits:
        if encircled_exit(grid, possible_exit):
            return grid, None
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == " ":
                grid[x][y] = 0
    x_enter, y_enter = exits[0]
    grid[x_enter][y_enter] = 1
    x_exit, y_exit = exits[1]
    grid[x_exit][y_exit] = 0
    k = 1
    while grid[x_exit][y_exit] == 0:
        make_step(grid, k)
        k += 1
        if k > len(grid) * len(grid[0]):
            return grid, None
    path = shortest_path(grid, (x_exit, y_exit))

    return grid, path


def add_path_to_grid(
    grid: List[List[Union[str, int]]], path: Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]
) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param path:
    :return:
    """

    if path:
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if (i, j) in path:
                    grid[i][j] = "X"
    return grid


if __name__ == "__main__":
    print(pd.DataFrame(bin_tree_maze(15, 15)))
    GRID = bin_tree_maze(15, 15)
    print(pd.DataFrame(GRID))
    _, PATH = solve_maze(GRID)
    MAZE = add_path_to_grid(GRID, PATH)
    print(pd.DataFrame(MAZE))
