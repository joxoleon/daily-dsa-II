# [ Name: Number of Islands ]  [ Category: graphs ]  [ Topic: graphs ]  [ Weight: 10 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/number-of-islands/ ]

"""
Given a 2D grid of '1's (land) and '0's (water), count the number of distinct islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. The grid is rectangular and may be empty. Return the number of islands.
Example: Given grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
], the output is 3.
"""

from typing import List

def numIslands(grid: List[List[str]]) -> int:
    pass

if __name__ == "__main__":
    assert numIslands([["1","1","0","0","0"],
                       ["1","1","0","0","0"],
                       ["0","0","1","0","0"],
                       ["0","0","0","1","1"]]) == 3
    assert numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]) == 1
    assert numIslands([["1","0","1","0"]]) == 2
    assert numIslands([["0"]]) == 0
    assert numIslands([["1"]]) == 1
    assert numIslands([]) == 0
    assert numIslands([["0","0","0"],["0","0","0"]]) == 0
    assert numIslands([["1","0","0","1"],["0","0","0","0"],["1","1","1","0"]]) == 3