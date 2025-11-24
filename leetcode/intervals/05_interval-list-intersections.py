# [ Name: Interval List Intersections ]  [ Category: intervals ]  [ Topic: intervals ]  [ Weight: 8 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/interval-list-intersections/ ]

"""
Given two lists of closed intervals, each list sorted and pairwise disjoint, return the intersection of these intervals.
Each interval is represented as [start, end].
Return the intersections as a list of intervals.
Constraints: 0 <= start <= end <= 10^9, list lengths up to 1000.
Example: Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
"""

from typing import List

def intervalIntersection(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    pass

if __name__ == "__main__":
    assert intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]) == [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    assert intervalIntersection([[1,3],[5,9]], []) == []
    assert intervalIntersection([], [[4,8],[10,12]]) == []
    assert intervalIntersection([[1,7]], [[3,10]]) == [[3,7]]
    assert intervalIntersection([[1,2],[3,4],[5,6]], [[2,3],[4,5],[6,7]]) == [[2,2],[3,3],[4,4],[5,5],[6,6]]
    assert intervalIntersection([[1,100]], [[50,200]]) == [[50,100]]
    assert intervalIntersection([[1,2],[3,4]], [[0,5]]) == [[1,2],[3,4]]
    assert intervalIntersection([[0,2]], [[3,4]]) == []
