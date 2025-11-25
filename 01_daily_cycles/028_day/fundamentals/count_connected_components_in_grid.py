# [ Name: Count Connected Components in Grid ]  [ Category: grids ]  [ Topic: dfs ]  [ Weight: 7 ]

"""
Problem Description:
Given a 2D grid of 0s and 1s, return the number of connected components formed by adjacent 1s (connected horizontally or vertically, not diagonally).
Input: grid as a list of lists, each element is 0 or 1; grid may be empty.
Output: integer count of distinct connected components of 1s.
Constraints:
- 1 <= rows, cols <= 100
- Only 0 or 1 in grid
Example:
Input: [[1,1,0],[0,1,0],[0,0,1]] -> Output: 2
"""

from typing import List

def count_components(grid: List[List[int]]) -> int:
    pass

if __name__ == "__main__":
    assert count_components([]) == 0
    assert count_components([[0]]) == 0
    assert count_components([[1]]) == 1
    assert count_components([[1,0,1,0]]) == 2
    assert count_components([[1,1],[0,0],[1,0]]) == 2
    assert count_components([[1,1,0],[0,1,0],[0,0,1]]) == 2
    assert count_components([[0,0],[0,0]]) == 0
    assert count_components([[1,1],[1,1]]) == 1
    assert count_components([[1,0,1],[0,1,0],[1,0,1]]) == 5

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")