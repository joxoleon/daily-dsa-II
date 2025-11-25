# [ Name: DP — Grid Minimum Path Sum ]  [ Category: dp ]  [ Topic: 2d_dp ]  [ Weight: 7 ]

"""
Problem Description:
Given a m x n grid filled with non-negative integers, find a path from the top-left to the bottom-right that minimizes the sum of all numbers along its path. You can only move either down or right at any point in time.

Constraints:
- 1 <= m, n <= 200
- 0 <= grid[i][j] <= 100

Example:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]] -> Output: 7
"""

from typing import List


def min_path_sum(grid: List[List[int]]) -> int:
    pass


if __name__ == "__main__":
    assert min_path_sum([[1,3,1],[1,5,1],[4,2,1]]) == 7
    assert min_path_sum([[1,2,3],[4,5,6]]) == 12
    assert min_path_sum([[1]]) == 1
    assert min_path_sum([[0,1],[1,0]]) == 1
    assert min_path_sum([[5,1,2],[4,10,1],[2,1,2]]) == 10
    assert min_path_sum([[7,4,8,1],[6,5,9,3],[2,3,2,7]]) == 25
    assert min_path_sum([[1,2],[1,1]]) == 3
    assert min_path_sum([[100,1],[1,100]]) == 102

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
