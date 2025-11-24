# [ Name: Skyline Problem ]  [ Category: extra_20_must_know ]  [ Topic: extra_20_must_know ]  [ Weight: 9 ]  [ Difficulty: Hard ]
# [ Link: https://leetcode.com/problems/the-skyline-problem/ ]

"""
Given a list of buildings represented by [left, right, height], return the skyline formed by these buildings as a list of [x, height] key points.
Input: buildings as List[List[int]].
Output: List[List[int]] representing the critical points of the skyline.
1 <= buildings.length <= 10000, 0 <= left < right <= 2^31-1, 1 <= height <= 2^31-1.
A key point is where the height changes.
Example: Input: [[2,9,10],[3,7,15],[5,12,12]] Output: [[2,10],[3,15],[7,12],[12,0],[9,10],[12,0]]
"""

from typing import List

def getSkyline(buildings: List[List[int]]) -> List[List[int]]:
    pass

if __name__ == "__main__":
    assert getSkyline([[2,9,10],[3,7,15],[5,12,12]]) == [[2,10],[3,15],[7,12],[12,0]]
    assert getSkyline([[1,2,1]]) == [[1,1],[2,0]]
    assert getSkyline([[0,2,3],[2,5,3]]) == [[0,3],[5,0]]
    assert getSkyline([[1,5,11],[2,6,7],[3,9,13],[12,16,7],[14,25,3],[19,22,18],[23,29,13],[24,28,4]]) == [[1,11],[3,13],[9,0],[12,7],[16,3],[19,18],[22,3],[23,13],[29,0]]
    assert getSkyline([[0,2147483647,2147483647]]) == [[0,2147483647],[2147483647,0]]
    assert getSkyline([]) == []
    assert getSkyline([[2,4,7],[2,4,5],[2,4,6]]) == [[2,7],[4,0]]
    assert getSkyline([[1,3,3],[2,4,4],[5,6,1]]) == [[1,3],[2,4],[4,0],[5,1],[6,0]]
