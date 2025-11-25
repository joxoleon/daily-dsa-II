# [ Name: Merge Two Sorted Interval Lists ]  [ Category: intervals ]  [ Topic: merge_two_lists ]  [ Weight: 5 ]

"""
Problem Description:
Given two lists of sorted, non-overlapping intervals, merge them into a single list of sorted, non-overlapping intervals.
An interval is a pair [start, end] with start <= end.
Return the merged list, preserving the order and merging overlapping intervals if necessary.

Constraints:
- Each interval list: length 0 <= n <= 10^4, with intervals sorted and non-overlapping.
- Intervals: 0 <= start <= end <= 10^9.

Example:
Input: a = [[1,3],[5,7]], b = [[2,6],[8,10]] -> Output: [[1,7],[8,10]]
"""

from typing import List

def merge_two_interval_lists(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    pass

if __name__ == "__main__":
    assert merge_two_interval_lists([[1,3],[5,7]], [[2,6],[8,10]]) == [[1,7],[8,10]]
    assert merge_two_interval_lists([], [[1,2],[3,4]]) == [[1,2],[3,4]]
    assert merge_two_interval_lists([[1,2],[5,6]], []) == [[1,2],[5,6]]
    assert merge_two_interval_lists([[1,2]], [[3,4]]) == [[1,2],[3,4]]
    assert merge_two_interval_lists([[1,5]], [[2,6]]) == [[1,6]]
    assert merge_two_interval_lists([[1,3],[4,6]], [[2,5]]) == [[1,6]]
    assert merge_two_interval_lists([[1,3],[7,9]], [[4,6]]) == [[1,3],[4,6],[7,9]]
    assert merge_two_interval_lists([[1,5],[10,14]], [[2,6],[8,10],[11,13]]) == [[1,6],[8,14]]

    print("All tests passed.")
