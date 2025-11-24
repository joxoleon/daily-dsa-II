# [ Name: Merge Overlapping Intervals ]  [ Category: intervals ]  [ Topic: merge_intervals ]  [ Weight: 9 ]

"""
Problem Description:
Given a list of intervals where each interval is a pair [start, end], merge all overlapping intervals and return a list of the merged intervals.
Each interval is a pair of integers [start, end] with start <= end.
Return the result as a list of non-overlapping intervals sorted by start time.
If there are no overlaps, return the intervals as-is.
An empty list should return an empty list.

Constraints:
- 0 <= len(intervals) <= 10^4
- -10^9 <= start <= end <= 10^9

Example:
Input: [[1,3],[2,6],[8,10],[15,18]] -> Output: [[1,6],[8,10],[15,18]]
"""

from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    pass

if __name__ == "__main__":
    assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert merge([[1,4],[4,5]]) == [[1,5]]
    assert merge([]) == []
    assert merge([[1,4],[0,4]]) == [[0,4]]
    assert merge([[1,4],[2,3]]) == [[1,4]]
    assert merge([[1,2],[3,4],[5,6]]) == [[1,2],[3,4],[5,6]]
    assert merge([[1,10],[2,9],[3,8]]) == [[1,10]]
    assert merge([[1,4],[2,5],[5,8],[9,10]]) == [[1,8],[9,10]]

    print("All tests passed.")
