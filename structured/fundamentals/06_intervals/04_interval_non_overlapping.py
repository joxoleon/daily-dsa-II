# [ Name: Erase Overlapping Intervals ]  [ Category: intervals ]  [ Topic: erase_overlap ]  [ Weight: 7 ]

"""
Problem Description:
Given a list of intervals where each interval is represented as [start, end], determine the minimum number of intervals you must remove to make the rest of the intervals non-overlapping.
Intervals may touch but not overlap.
Return an integer representing the minimum number of intervals to remove.

Constraints:
- 0 <= len(intervals) <= 10^5
- Each interval has 2 integers: [start, end] with start < end

Example:
Input: [[1,2],[2,3],[3,4],[1,3]] -> Output: 1
"""

from typing import List

def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    pass

if __name__ == "__main__":
    assert erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]]) == 1
    assert erase_overlap_intervals([[1,2],[1,2],[1,2]]) == 2
    assert erase_overlap_intervals([[1,2],[2,3]]) == 0
    assert erase_overlap_intervals([]) == 0
    assert erase_overlap_intervals([[1,10],[2,3],[4,5],[6,7],[8,9]]) == 1
    assert erase_overlap_intervals([[1,100],[11,22],[1,11],[2,12]]) == 2
    assert erase_overlap_intervals([[1,2]]) == 0
    assert erase_overlap_intervals([[0,2],[1,3],[2,4],[3,5],[4,6]]) == 2

    print("All tests passed.")
