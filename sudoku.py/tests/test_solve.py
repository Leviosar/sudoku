from sudoku_py import solve

def test_solvable_matrix():
    matrix = [
        [0, 4, 0, 9, 0, 0, 3, 8, 0],
        [6, 0, 0, 0, 0, 0, 0, 9, 0],
        [2, 9, 0, 3, 7, 4, 5, 0, 0],
        [0, 1, 7, 0, 9, 6, 0, 2, 3],
        [0, 0, 0, 2, 0, 0, 0, 5, 4],
        [8, 0, 4, 7, 0, 0, 0, 0, 0],
        [0, 0, 2, 5, 3, 0, 9, 0, 8],
        [4, 0, 0, 0, 2, 7, 6, 0, 1],
        [0, 8, 1, 0, 0, 0, 2, 7, 0],
    ]

    solutions = []
    solve(matrix, solutions)
    
    assert len(solutions) == 1

def test_unsolvable_matrix():
    matrix = [
        [0, 3, 0, 0, 7, 2, 1, 0, 4],
        [0, 2, 0, 3, 8, 4, 0, 6, 5],
        [9, 0, 8, 0, 0, 0, 7, 0, 2],
        [1, 8, 0, 7, 9, 6, 0, 0, 3],
        [0, 5, 0, 2, 0, 1, 6, 0, 0],
        [6, 0, 0, 4, 5, 0, 2, 1, 0],
        [8, 1, 4, 0, 0, 0, 0, 9, 0],
        [3, 6, 7, 0, 4, 9, 5, 0, 0],
        [0, 9, 5, 0, 0, 3, 8, 0, 7],
    ]

    solutions = []
    solve(matrix, solutions)
    
    print(solutions)
    
    assert len(solutions) == 2