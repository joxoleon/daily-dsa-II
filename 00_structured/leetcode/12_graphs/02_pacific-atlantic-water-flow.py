# [ Name: Pacific Atlantic Water Flow ]  [ Category: graphs ]  [ Topic: graphs ]  [ Weight: 8 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/pacific-atlantic-water-flow/ ]

"""
Given an m x n matrix of non-negative integers representing heights, water can flow from a cell to another adjacent cell if the next cell's height is less than or equal to the current cell's. The Pacific Ocean touches the matrix's left and top edges, while the Atlantic touches the right and bottom edges. Return coordinates where water can flow to both oceans.
Inputs: matrix (List[List[int]])
Output: List of [row, col] coordinates
Constraints: 1 <= m, n <= 200; 0 <= height <= 10^5
Example: Input: [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]] -> Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
"""

from typing import List

def pacificAtlantic(matrix: List[List[int]]) -> List[List[int]]:
    pass

if __name__ == "__main__":
    assert sorted(pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])) == sorted([[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]])
    assert pacificAtlantic([]) == []
    assert pacificAtlantic([[1]]) == [[0,0]]
    assert pacificAtlantic([[3,3,3],[3,3,3],[3,3,3]]) == [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    assert sorted(pacificAtlantic([[1,2],[4,3]])) == sorted([[0,1],[1,0],[1,1]])
    assert pacificAtlantic([[10]]) == [[0,0]]
    assert sorted(pacificAtlantic([[5,5,5],[5,1,5],[5,5,5]])) == sorted([[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]])
    assert pacificAtlantic([[0,0],[0,0]]) == [[0,0],[0,1],[1,0],[1,1]]
