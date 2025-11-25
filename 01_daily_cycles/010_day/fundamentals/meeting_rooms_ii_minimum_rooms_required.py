# [ Name: Meeting Rooms II — Minimum Rooms Required ]  [ Category: intervals ]  [ Topic: min_rooms ]  [ Weight: 8 ]

"""
Problem Description:
Given an array of meeting time intervals where each interval is a pair [start, end], return the minimum number of meeting rooms required to host all meetings without overlaps.

- Input: List of intervals with integer start and end (0 <= start < end <= 10^6, 0 <= len(intervals) <= 10^4)
- Output: Integer representing the minimum number of rooms required.
- If no meetings are scheduled, return 0.
- Meetings may touch but not overlap (e.g., end == start is allowed).

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
    assert min_meeting_rooms([[1,5],[8,9],[8,10]]) == 2
    assert min_meeting_rooms([[1,4],[2,5],[7,9]]) == 2
    assert min_meeting_rooms([[13,15],[1,13]]) == 1
    assert min_meeting_rooms([[0,5],[5,10],[10,15],[15,20]]) == 1
    assert min_meeting_rooms([[1,10],[2,7],[3,19],[8,12],[10,20],[11,30]]) == 4

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
