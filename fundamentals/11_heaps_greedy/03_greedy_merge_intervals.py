# [ Name: Greedy — Merge Intervals ]  [ Category: greedy ]  [ Topic: intervals ]  [ Weight: 9 ]

"""
Problem Description:
Given a list of intervals where each interval is a pair of integers [start, end], merge all overlapping intervals and return the merged list in any order.
Each interval includes both start and end.
If there are no overlaps, return the original list.
Assume 0 <= start <= end <= 10^6, and 0 <= len(intervals) <= 10^4.

Example:
Input: [[1,3],[2,6],[8,10],[15,18]] -> Output: [[1,6],[8,10],[15,18]]
"""

from typing import List

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    pass

if __name__ == "__main__":
    assert merge_intervals([]) == []
    assert merge_intervals([[1,2]]) == [[1,2]]
    assert merge_intervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert merge_intervals([[1,4],[4,5]]) == [[1,5]]
    assert merge_intervals([[1,4],[0,2],[3,5]]) == [[0,5]]
    assert merge_intervals([[1,4],[2,3]]) == [[1,4]]
    assert merge_intervals([[5,7],[1,3],[2,4],[8,10]]) == [[1,4],[5,7],[8,10]]
    assert merge_intervals([[1,10],[2,6],[3,7],[8,9]]) == [[1,10]]

    print("All tests passed.")
