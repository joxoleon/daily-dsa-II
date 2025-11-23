# [ Name: Shortest Path in a Grid ]  [ Category: grids ]  [ Topic: bfs ]  [ Weight: 8 ]

"""
Problem Description:
Given an m x n grid of 0s and 1s, find the length of the shortest path from the top-left to the bottom-right cell.
You can move up, down, left, or right to any cell with value 0. Cells with value 1 are obstacles and cannot be visited.
Return the minimum number of steps required for the path, or -1 if no such path exists.

Constraints:
- 1 <= m, n <= 100
- The starting and ending cells can be obstacles.
- Output: integer (minimum steps or -1).

Example:
Input: grid = [[0,0,1],[1,0,0],[1,1,0]] -> Output: 5
"""

from typing import List

def shortest_path(grid: List[List[int]]) -> int:
    pass

if __name__ == "__main__":
    assert shortest_path([[0,0,1],[1,0,0],[1,1,0]]) == 5
    assert shortest_path([[0,1],[1,0]]) == -1
    assert shortest_path([[0]]) == 1
    assert shortest_path([[1]]) == -1
    assert shortest_path([[0,0,0],[0,1,0],[0,0,0]]) == 5
    assert shortest_path([[0,1,0,0],[0,1,1,0],[0,0,0,0]]) == 7
    assert shortest_path([[0,0,0,1],[1,1,0,1],[0,0,0,0]]) == 6
    assert shortest_path([[1,0,0],[1,1,0],[0,0,0]]) == -1
    print("All tests passed.")
