#!/usr/bin/python3
"""
This module contains a function to rotate a 2D matrix.

The function `rotate_2d_matrix` takes a 2D matrix as input
and rotates it 90 degrees clockwise.
The input matrix is modified in-place.

Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

rotate_2d_matrix(matrix)

After rotation, the matrix will be:
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise.

    Args:
        matrix (list): The 2D matrix to be rotated.

    Returns:
        None: The function modifies the input matrix in-place.

    Raises:
        None: No specific exceptions are raised.

    """
    if not isinstance(matrix, list):
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: isinstance(x, list), matrix)):
        return
    rows = len(matrix)
    cols = len(matrix[0])
    if not all(map(lambda x: len(x) == cols, matrix)):
        return
    c, r = 0, rows - 1
    for i in range(cols * rows):
        if i % rows == 0:
            matrix.append([])
        if r == -1:
            r = rows - 1
            c += 1
        matrix[-1].append(matrix[r][c])
        if c == cols - 1 and r >= -1:
            matrix.pop(r)
        r -= 1
