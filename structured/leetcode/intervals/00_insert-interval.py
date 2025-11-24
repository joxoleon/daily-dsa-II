# [ Name: Insert Interval ]  [ Category: intervals ]  [ Topic: intervals ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/insert-interval/ ]

"""
Given a list of non-overlapping intervals sorted by start time, insert a new interval 
so that the resulting list remains sorted and non-overlapping by merging if necessary.
Return the new list of intervals.
Intervals are given as List[List[int]]. 1 <= intervals.length <= 10^4. 
0 <= intervals[i][0] <= intervals[i][1] <= 10^5. newInterval is List[int] in the same format.
Example: intervals = [[1,3],[6,9]], newInterval = [2,5] → Output: [[1,5],[6,9]]
"""

from typing import List

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    pass

if __name__ == "__main__":
    assert insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
    assert insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
    assert insert([], [5,7]) == [[5,7]]
    assert insert([[1,5]], [2,3]) == [[1,5]]
    assert insert([[1,5]], [2,7]) == [[1,7]]
    assert insert([[1,5]], [6,8]) == [[1,5],[6,8]]
    assert insert([[1,2],[3,4]], [5,6]) == [[1,2],[3,4],[5,6]]
    assert insert([[1,2],[5,6]], [3,4]) == [[1,2],[3,4],[5,6]]