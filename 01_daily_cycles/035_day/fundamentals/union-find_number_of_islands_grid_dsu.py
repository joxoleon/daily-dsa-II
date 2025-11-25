# [ Name: Union-Find — Number of Islands (Grid DSU) ]  [ Category: union_find ]  [ Topic: grid_dsu ]  [ Weight: 8 ]

"""
Problem Description:
Given a 2D grid of '1's (land) and '0's (water), count the number of distinct islands.
Islands are formed by connecting adjacent lands horizontally or vertically.
Return the total number of islands in the grid.

Constraints:
- 1 <= number of rows, columns <= 300
- grid[i][j] is either '0' or '1'

Example:
Input: [["1","1","0","0"],["1","0","0","1"],["0","0","1","1"]] -> Output: 3
"""

from typing import List

def num_islands(grid: List[List[str]]) -> int:
    pass

if __name__ == "__main__":
    assert num_islands([["1"]]) == 1
    assert num_islands([["0"]]) == 0
    assert num_islands([["1","1","1"],["1","1","1"]]) == 1
    assert num_islands([["1","0","1"],["0","1","0"],["1","0","1"]]) == 5
    assert num_islands([["0","0","0"],["0","0","0"]]) == 0
    assert num_islands([["1","0","0","1"],["0","0","1","0"],["1","1","0","0"]]) == 4
    assert num_islands([["1","1","0","0"],["1","0","0","1"],["0","0","1","1"]]) == 3
    assert num_islands([["1","0","1"],["0","1","0"],["1","1","1"]]) == 2

    print("All tests passed.")
