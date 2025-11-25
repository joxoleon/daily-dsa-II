# [ Name: DFS on a Grid — Explore Region ]  [ Category: grids ]  [ Topic: dfs ]  [ Weight: 5 ]

"""
Problem Description:
Given a 2D grid of integers and a starting cell (r, c), explore and count the number of connected cells (horizontally or vertically, not diagonally) that have the same value as grid[r][c].
The connection must remain within the grid, and only cells matching the value of grid[r][c] are counted.
Input: grid (List[List[int]]), integers r and c (starting position), and an integer target.
Return the size of the connected region explored. If the starting cell does not equal target, return 0.

Constraints:
- 1 <= len(grid), len(grid[0]) <= 50
- 0 <= r < len(grid), 0 <= c < len(grid[0])
- grid only contains integers

Example:
Input: grid = [[1,2,1],[1,1,0],[0,1,1]], r = 1, c = 1, target = 1 -> Output: 5
"""

from typing import List

def grid_dfs(grid: List[List[int]], r: int, c: int, target: int) -> int:
    pass

if __name__ == "__main__":
    assert grid_dfs([[1,2,1],[1,1,0],[0,1,1]], 1, 1, 1) == 5
    assert grid_dfs([[2,2,2],[2,3,3],[2,2,2]], 1, 1, 2) == 0
    assert grid_dfs([[0]], 0, 0, 0) == 1
    assert grid_dfs([[4,4],[4,5]], 0, 1, 4) == 3
    assert grid_dfs([[1,2,2],[2,2,1],[1,2,2]], 1, 1, 2) == 5
    assert grid_dfs([[7,8,7],[8,7,8],[7,8,7]], 1, 1, 8) == 0
    assert grid_dfs([[6,6,6],[6,6,6],[6,6,6]], 0, 0, 6) == 9
    assert grid_dfs([[3,5,3,3,3],[5,5,5,5,5],[3,5,3,3,3]], 0, 0, 3) == 5

    print("All tests passed.")
