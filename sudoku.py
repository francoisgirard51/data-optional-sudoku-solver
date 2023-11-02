# pylint: disable=missing-docstring
"""This code is a Sudoku solver
"""

def is_valid_grid(grid):
    """We need to have a preset grid first
    """
    return True

def find_empty_location(grid, location):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                location[0] = row
                location[1] = col
                return True
    return False

def used_in_row(grid, row, num):
    for i in range(9):
        if grid[row][i] == num:
            return True
    return False

def used_in_col(grid, col, num):
    for i in range(9):
        if grid[i][col] == num:
            return True
    return False

def used_in_box(grid, row, col, num):
    for i in range(3):
        for j in range(3):
            if grid[i + row][j + col] == num:
                return True
    return False

def is_safe(grid, row, col, num):
    return (not used_in_row(grid, row, num) and
            not used_in_col(grid, col, num) and
            not used_in_box(grid, row - row % 3, col - col % 3, num))

def sudoku_solver(grid):
    try:
        if not isinstance(grid, list) or \
           len(grid) != 9 or \
           not all(isinstance(row, list) and len(row) == 9 for row in grid):
            return "invalid grid"

        if not is_valid_grid(grid):
            return "invalid grid"

        if solve(grid):
            return grid
        return "invalid grid"
    except Exception as element:
        return "invalid grid"

def solve(grid):
    empty_location = [0, 0]
    if not find_empty_location(grid, empty_location):
        return True

    row, col = empty_location

    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num

            if solve(grid):
                return True

            grid[row][col] = 0

    return False
