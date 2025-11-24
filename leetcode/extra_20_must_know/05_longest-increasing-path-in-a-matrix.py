# [ Name: Longest Increasing Path in a Matrix ]  [ Category: extra_20_must_know ]  [ Topic: extra_20_must_know ]  [ Weight: 9 ]  [ Difficulty: Hard ]
# [ Link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/ ]

"""
Given an m x n integer matrix, find the length of the longest increasing path in the matrix.
From each cell, you can move in four directions (up, down, left, right) to an adjacent cell with a strictly larger value.
Return the length of the longest increasing path.
1 <= m, n <= 200; -2^31 <= matrix[i][j] <= 2^31 - 1
Example: For matrix = [[9,9,4],[6,6,8],[2,1,1]], output is 4.
"""

from typing import List

def longestIncreasingPath(matrix: List[List[int]]) -> int:
    pass

if __name__ == "__main__":
    assert longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]) == 4
    assert longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]) == 4
    assert longestIncreasingPath([[1]]) == 1
    assert longestIncreasingPath([[7,7,7],[7,7,7],[7,7,7]]) == 1
    assert longestIncreasingPath([[1,2,3,4]]) == 4
    assert longestIncreasingPath([[4],[3],[2],[1]]) == 4
    assert longestIncreasingPath([[1,2],[3,4]]) == 4
    assert longestIncreasingPath([[0,1,2,3,2,1,0]]) == 4
    assert longestIncreasingPath([[10,-1,2],[3,4,5],[6,7,8]]) == 6