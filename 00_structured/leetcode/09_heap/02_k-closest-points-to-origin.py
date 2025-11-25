# [ Name: K Closest Points to Origin ]  [ Category: heap ]  [ Topic: heap ]  [ Weight: 8 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/k-closest-points-to-origin/ ]

"""
Given an array 'points' where points[i] = [xi, yi] represents a point on the X-Y plane, return the k closest points to the origin (0, 0).
Inputs: points (List[List[int]]), k (int).
Output: List[List[int]] containing k points closest to the origin.
1 <= k <= points.length <= 10^4, Coordinates are integers in [-10^4, 10^4].
Distance is calculated by Euclidean distance. Answer can be returned in any order.
Example: Input: points = [[1,3],[-2,2]], k = 1; Output: [[-2,2]].
"""

from typing import List

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    pass

if __name__ == "__main__":
    assert sorted(kClosest([[1,3],[-2,2]], 1)) == [[-2,2]]
    assert sorted(kClosest([[3,3],[5,-1],[-2,4]], 2)) in ([[3,3],[-2,4]], [[-2,4],[3,3]])
    assert sorted(kClosest([[0,1],[1,0]], 2)) == [[0,1],[1,0]]
    assert sorted(kClosest([[5,8],[1,2],[0,1]], 2)) in ([[1,2],[0,1]], [[0,1],[1,2]])
    assert sorted(kClosest([[1,1],[2,2],[3,3]], 1)) == [[1,1]]
    assert sorted(kClosest([[2,2],[1,1],[0,0]], 3)) == [[2,2],[1,1],[0,0]]
    assert sorted(kClosest([[1,3],[-2,2],[2,-2]], 2)) in ([[-2,2],[2,-2]], [[2,-2],[-2,2]])
    assert sorted(kClosest([[0,0]], 1)) == [[0,0]]