# [ Name: Meeting Rooms — Can Attend All ]  [ Category: intervals ]  [ Topic: overlap_check ]  [ Weight: 8 ]

"""
Problem Description:
Given an array of meeting time intervals where each interval is a pair [start, end], determine if a person can attend all meetings without any overlaps.
Return True if no two meetings overlap, otherwise return False.

Constraints:
- Input: List of intervals [[start1, end1], [start2, end2], ...], where 0 <= start < end <= 10^6
- 0 <= number of intervals <= 10^4

Example:
Input: [[0, 30], [35, 50], [60, 70]] -> Output: True
"""

from typing import List

def can_attend_meetings(intervals: List[List[int]]) -> bool:
    pass

if __name__ == "__main__":
    assert can_attend_meetings([[0, 30], [35, 50], [60, 70]]) == True
    assert can_attend_meetings([[5, 10], [0, 4]]) == True
    assert can_attend_meetings([[0, 5], [4, 10]]) == False
    assert can_attend_meetings([]) == True
    assert can_attend_meetings([[1, 3], [2, 6], [8, 10]]) == False
    assert can_attend_meetings([[12, 15]]) == True
    assert can_attend_meetings([[1, 5], [6, 10], [10, 15]]) == True
    assert can_attend_meetings([[0, 10], [10, 20], [19, 30]]) == False

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
