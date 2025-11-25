# [ Name: Greedy — Non-Overlapping Intervals ]  [ Category: greedy ]  [ Topic: intervals ]  [ Weight: 9 ]

"""
Problem Description:
Given a list of intervals represented as [start, end], return the minimum number of intervals you must remove to make the rest non-overlapping.
Intervals are closed at the start and open at the end.
Return 0 if no intervals need to be removed.

Constraints:
- 0 <= len(intervals) <= 10^4
- Each interval: [start, end] with start < end

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
    assert erase_overlap_intervals([[1,100],[11,22],[1,11],[2,12]]) == 2
    assert erase_overlap_intervals([[0,2],[1,3],[2,4],[3,5],[4,6]]) == 2
    assert erase_overlap_intervals([[1,5],[2,3],[3,4],[4,5]]) == 1
    assert erase_overlap_intervals([[1,3]]) == 0

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")