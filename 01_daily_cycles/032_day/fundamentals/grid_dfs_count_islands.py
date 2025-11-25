# [ Name: Grid DFS — Count Islands ]  [ Category: graphs ]  [ Topic: grid_dfs ]  [ Weight: 6 ]

"""
Problem Description:
Given a 2D grid of 0s and 1s, return the number of islands.
An island is a group of adjacent 1s (connected horizontally or vertically).
The grid will have at least 1 row and 1 column.
Only 0 (water) and 1 (land) are valid grid values.

Constraints:
- 1 <= number of rows, columns <= 100
- Input: List[List[int]]
- Output: integer (number of islands)

Example:
Input: [[1,1,0,0],[0,1,0,1],[1,0,0,1]] -> Output: 3
"""

from typing import List

def count_islands(grid: List[List[int]]) -> int:
    pass

if __name__ == "__main__":
    assert count_islands([[1]]) == 1
    assert count_islands([[0]]) == 0
    assert count_islands([[1,1,0],[0,1,0],[1,0,1]]) == 3
    assert count_islands([[1,0,1,0],[0,0,0,1],[1,1,0,0]]) == 4
    assert count_islands([[0,0,0],[0,0,0]]) == 0
    assert count_islands([[1,1,1],[1,1,1]]) == 1
    assert count_islands([[1,0,1,0,1,0,1]]) == 4
    assert count_islands([[1,0,0],[0,1,1],[0,1,0]]) == 2

    print("All tests passed.")
