# [ Name: Max Points on a Line ]  [ Category: extra_20_must_know ]  [ Topic: extra_20_must_know ]  [ Weight: 8 ]  [ Difficulty: Hard ]
# [ Link: https://leetcode.com/problems/max-points-on-a-line/ ]

"""
Given an array points where points[i] = [xi, yi] represents a point on a 2D plane, return the maximum number of points that lie on the same straight line.
1 <= points.length <= 300
points[i].length == 2
-10^4 <= xi, yi <= 10^4
Example: Input: points = [[1,1],[2,2],[3,3]] Output: 3
"""

from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        pass

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxPoints([[1,1],[2,2],[3,3]]) == 3
    assert sol.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]) == 4
    assert sol.maxPoints([[0,0]]) == 1
    assert sol.maxPoints([[0,0],[1,1],[0,0]]) == 3
    assert sol.maxPoints([[1,1],[1,1],[1,1]]) == 3
    assert sol.maxPoints([[2,3],[3,3],[-5,3]]) == 3
    assert sol.maxPoints([[0,0],[94911151,94911150],[94911152,94911151]]) == 2
    assert sol.maxPoints([[1,0],[0,0],[1,-1]]) == 2