# [ Name: Multi-Source BFS on Grid ]  [ Category: grids ]  [ Topic: bfs ]  [ Weight: 6 ]

"""
Problem Description:
Given a 2D grid of integers where 0 represents an empty cell and 1 represents an obstacle, and a list of source coordinates, return the minimum number of steps to reach the farthest empty cell from any source, moving in 4 directions.
If there are no empty cells, return 0.
If an empty cell is unreachable, return -1.

Constraints:
- 1 <= number of rows, columns <= 100
- 0 <= grid[i][j] <= 1
- 0 <= coordinates in sources < grid dimensions

Example:
Input: grid = [[0,1,0],[0,0,1],[1,0,0]], sources = [(0,0)]
Output: 4
"""

from typing import List, Tuple

def multi_source_bfs(grid: List[List[int]], sources: List[Tuple[int,int]]) -> int:
    pass

if __name__ == "__main__":
    assert multi_source_bfs([[0,1,0],[0,0,1],[1,0,0]], [(0,0)]) == 4
    assert multi_source_bfs([[1,1],[1,1]], [(0,0)]) == 0
    assert multi_source_bfs([[0,0,0],[0,1,0],[0,0,0]], [(1,0), (1,2)]) == 2
    assert multi_source_bfs([[0]], [(0,0)]) == 0
    assert multi_source_bfs([[0,1,0],[1,1,0],[0,0,0]], [(0,2)]) == 4
    assert multi_source_bfs([[0,1,1],[1,1,1],[1,1,0]], [(0,0)]) == -1
    assert multi_source_bfs([[0,0],[0,1]], [(0,1)]) == 2
    assert multi_source_bfs([[1]], [(0,0)]) == 0

    print("All tests passed.")
