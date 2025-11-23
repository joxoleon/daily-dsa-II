# [ Name: BFS on a Grid — Explore Region ]  [ Category: grids ]  [ Topic: bfs ]  [ Weight: 5 ]

"""
Problem Description:
Given a 2D grid of 0s and 1s, starting from a cell (r, c), count the size of the connected region of 1s using BFS.
Cells are connected 4-directionally (up, down, left, right).
Return the total number of cells in the region, or 0 if (r, c) is out of bounds or not a 1.

Constraints:
- 1 <= len(grid), len(grid[0]) <= 100
- Only inputs 0 or 1 in the grid.

Example:
Input: grid = [[1,1,0],[1,0,0]], r = 0, c = 0 -> Output: 3
"""

from typing import List

def grid_bfs(grid: List[List[int]], r: int, c: int) -> int:
    pass

if __name__ == "__main__":
    assert grid_bfs([[1,1,0],[1,0,0]], 0, 0) == 3
    assert grid_bfs([[1,1,0],[1,0,1]], 1, 2) == 1
    assert grid_bfs([[0,0],[0,0]], 0, 0) == 0
    assert grid_bfs([[1,0,1],[0,1,0],[1,0,1]], 0, 2) == 1
    assert grid_bfs([[1,1,1],[1,1,1],[1,1,1]], 2, 2) == 9
    assert grid_bfs([[1]], 0, 0) == 1
    assert grid_bfs([[1,0],[0,1]], 1, 1) == 1
    assert grid_bfs([[0]], 0, 0) == 0

    print("All tests passed.")
