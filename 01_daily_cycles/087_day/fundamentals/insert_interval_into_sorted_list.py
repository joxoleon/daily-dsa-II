# [ Name: Insert Interval Into Sorted List ]  [ Category: intervals ]  [ Topic: insert_interval ]  [ Weight: 7 ]

"""
Problem Description:
Given a sorted list of non-overlapping intervals, insert a new interval and merge if necessary.
Each interval is represented as a list of two integers [start, end].
Return the resulting list of non-overlapping intervals in sorted order.
Assume intervals and the new interval are closed and both start and end are inclusive.
Constraints: intervals is sorted by start; 0 <= len(intervals) <= 10^4.

Example:
Input: intervals = [[1,3],[6,9]], new = [2,5] -> Output: [[1,5],[6,9]]
"""

from typing import List

def insert(intervals: List[List[int]], new: List[int]) -> List[List[int]]:
    pass

if __name__ == "__main__":
    assert insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
    assert insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
    assert insert([], [5,7]) == [[5,7]]
    assert insert([[1,5]], [2,3]) == [[1,5]]
    assert insert([[1,5]], [6,8]) == [[1,5],[6,8]]
    assert insert([[1,5]], [0,0]) == [[0,0],[1,5]]
    assert insert([[1,5]], [0,3]) == [[0,5]]
    assert insert([[1,2],[3,4]], [5,6]) == [[1,2],[3,4],[5,6]]
    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
