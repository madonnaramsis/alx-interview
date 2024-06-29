#!/usr/bin/python3
"""
This module contains a function for computing the perimeter
of an island with no lakes.
"""


def island_perimeter(grid):
    """
    Computes the perimeter of an island with no lakes.

    Args:
        grid (list): A 2D grid representing the island,
        where 1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.

    Raises:
        None

    Examples:
        >>> grid = [[0, 1, 0, 0],
        ...         [1, 1, 1, 0],
        ...         [0, 1, 0, 0],
        ...         [1, 1, 0, 0]]
        >>> island_perimeter(grid)
        16
    """
    perimeter = 0
    if type(grid) is not list:
        return 0
    n = len(grid)
    for i, row in enumerate(grid):
        m = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == m - 1 or (m > j + 1 and row[j + 1] == 0),
                i == n - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
