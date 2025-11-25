# [ Name: Greedy — Meeting Rooms Required ]  [ Category: greedy ]  [ Topic: meetings ]  [ Weight: 7 ]

"""
Problem Description:
Given an array of meeting time intervals where intervals[i] = [start_i, end_i], determine the minimum number of meeting rooms required so that no meetings overlap.
Return an integer representing the least number of rooms needed.
Assume start_i < end_i and intervals length is between 0 and 10^4.
If there are no intervals, return 0.

Example:
Input: [[0,30],[5,10],[15,20]] -> Output: 2
"""

from typing import List

def min_meeting_rooms(intervals: List[List[int]]) -> int:
    pass

if __name__ == "__main__":
    assert min_meeting_rooms([[0,30],[5,10],[15,20]]) == 2
    assert min_meeting_rooms([[7,10],[2,4]]) == 1
    assert min_meeting_rooms([]) == 0
    assert min_meeting_rooms([[1,5],[5,10],[10,15]]) == 1
    assert min_meeting_rooms([[1,10],[2,3],[3,4],[4,5],[5,6]]) == 2
    assert min_meeting_rooms([[1,3],[2,6],[8,10],[15,18]]) == 2
    assert min_meeting_rooms([[1,2],[2,3],[3,4],[4,5],[5,6]]) == 1
    assert min_meeting_rooms([[1,10],[2,7],[3,19],[8,12],[10,20],[11,30]]) == 4

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
