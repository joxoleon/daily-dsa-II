# [ Name: Meeting Rooms ]  [ Category: intervals ]  [ Topic: intervals ]  [ Weight: 7 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/meeting-rooms/ ]

"""
Given an array of meeting time intervals where each interval is a pair [start, end], determine if a person could attend all meetings. Return True if there are no overlapping intervals, otherwise return False. Each meeting's start and end times are non-negative integers and start < end. 
Example: Input: intervals = [[0,30],[5,10],[15,20]], Output: False
"""

from typing import List

def canAttendMeetings(intervals: List[List[int]]) -> bool:
    pass

if __name__ == "__main__":
    assert canAttendMeetings([[0,30],[5,10],[15,20]]) == False
    assert canAttendMeetings([[7,10],[2,4]]) == True
    assert canAttendMeetings([]) == True
    assert canAttendMeetings([[1,5]]) == True
    assert canAttendMeetings([[1,3],[3,5],[6,8]]) == True
    assert canAttendMeetings([[1,5],[2,6]]) == False
    assert canAttendMeetings([[5,10],[10,15],[15,20]]) == True
    assert canAttendMeetings([[0,5],[5,10],[9,12]]) == False