# [ Name: Non-overlapping Intervals ]  [ Category: intervals ]  [ Topic: intervals ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/non-overlapping-intervals/ ]

"""
Given an array 'intervals' where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove so that the remaining intervals do not overlap.
1 <= intervals.length <= 10^5; intervals[i].length == 2
0 <= starti < endi <= 10^6
Example: intervals = [[1,2],[2,3],[3,4],[1,3]] → Output: 1
"""

from typing import List

def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    pass

if __name__ == "__main__":
    assert eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1
    assert eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2
    assert eraseOverlapIntervals([[1,2],[2,3]]) == 0
    assert eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]) == 2
    assert eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]) == 2
    assert eraseOverlapIntervals([[1,5],[2,3],[3,4],[4,5]]) == 1
    assert eraseOverlapIntervals([[1,2]]) == 0
    assert eraseOverlapIntervals([[1,10],[2,3],[3,4],[4,5],[6,7]]) == 1