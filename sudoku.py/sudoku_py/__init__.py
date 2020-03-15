__version__ = '0.1.0'

import numpy as np

from pprint import pprint
from typing import Callable, List

def possible(matrix: List[List[int]], x: int, y: int, n:int) -> bool:
    """
    Based on sudoku's rules, checks if a integer n can be placed in matrix[x][y]
    without breaking the game. Return true if test pass, false otherwise
    """

    # Check for problem in row
    for i in range(0, 9):
        if matrix[x][i] == n:
            return False

    # Check for problem in column
    for j in range(0, 9):
        if matrix[j][y] == n:
            return False
    
    # Initial indexes for inner square
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3

    # Check for problem in inner square
    for i in range(0, 3):
        for j in range(0, 3):
            if matrix[x0 + i][y0 + j] == n:
                return False
    
    return True

def solve(inputMatrix: List[List[int]] = []):
    """
    Recursive implementation of a brute force 9x9 sudoku solver, loops for
    every element on a matrix until finds a 0 (blank space) to fill, then tries
    all possible numbers for that space, if it has a match, the function calls itself,
    otherwise return None.

    After finding one solution, appends the resultant matrix to the solutions list and 
    continues to find other possible solutions
    """

    global matrix
    if matrix == []:
        matrix = inputMatrix

    for x in range(9):
        for y in range(9):
            if matrix[x][y] == 0:
                for n in range(1, 10):
                    if possible(matrix, x, y, n):
                        matrix[x][y] = n
                        solve()
                        matrix[x][y] = 0
                return

    # Searches for zeros inside the matrix, if any zero show up
    # it means it's a false positive and remove from solutions list
    print(np.matrix(matrix))
    input("Continue?")
    return


matrix: List[List[int]] = []

solve([
    [0, 3, 0, 0, 7, 2, 1, 0, 4],
    [0, 2, 0, 3, 8, 4, 0, 6, 5],
    [9, 0, 8, 0, 0, 0, 7, 0, 2],
    [1, 8, 0, 7, 9, 6, 0, 0, 3],
    [0, 5, 0, 2, 0, 1, 6, 0, 0],
    [6, 0, 0, 4, 5, 0, 2, 1, 0],
    [8, 1, 4, 0, 0, 0, 0, 9, 0],
    [3, 6, 7, 0, 4, 9, 5, 0, 0],
    [0, 9, 5, 0, 0, 3, 8, 0, 7],
])