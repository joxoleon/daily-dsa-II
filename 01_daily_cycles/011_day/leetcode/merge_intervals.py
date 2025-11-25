# [ Name: Merge Intervals ]  [ Category: intervals ]  [ Topic: intervals ]  [ Weight: 10 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/merge-intervals/ ]

"""
Given a collection of intervals, merge all overlapping intervals.
Input: List of intervals where each interval is a list of two integers [start, end].
Output: A list of merged non-overlapping intervals sorted by the start times.
1 <= intervals.length <= 10^4
Intervals have 0 <= start <= end <= 10^4.
Example: Input: [[1,3],[2,6],[8,10],[15,18]] Output: [[1,6],[8,10],[15,18]]
"""

from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    pass

if __name__ == "__main__":
    assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert merge([[1,4],[4,5]]) == [[1,5]]
    assert merge([[1,4],[2,3]]) == [[1,4]]
    assert merge([[1,4],[0,4]]) == [[0,4]]
    assert merge([[1,4],[0,1]]) == [[0,4]]
    assert merge([[1,4],[2,5],[7,9]]) == [[1,5],[7,9]]
    assert merge([[1,4],[5,6]]) == [[1,4],[5,6]]
    assert merge([[2,3],[4,5],[6,7],[8,9],[1,10]]) == [[1,10]]
