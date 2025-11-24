# [ Name: Meeting Rooms II ]  [ Category: intervals ]  [ Topic: intervals ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/meeting-rooms-ii/ ]

"""
Given an array of meeting time intervals consisting of start and end times, determine the minimum number of conference rooms required. Each interval is a pair [start, end). Return an integer representing the minimum conference rooms needed.
Constraints: 1 <= intervals.length <= 10^4, 0 <= start < end <= 10^6.
Example: intervals = [[0,30],[5,10],[15,20]] ⇒ Output: 2
"""

from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        pass

if __name__ == "__main__":
    sol = Solution()
    assert sol.minMeetingRooms([[0,30],[5,10],[15,20]]) == 2
    assert sol.minMeetingRooms([[7,10],[2,4]]) == 1
    assert sol.minMeetingRooms([[1,5],[8,9],[8,9]]) == 2
    assert sol.minMeetingRooms([[1,10],[2,7],[3,19],[8,12],[10,20],[11,30]]) == 4
    assert sol.minMeetingRooms([]) == 0
    assert sol.minMeetingRooms([[1,2]]) == 1
    assert sol.minMeetingRooms([[1,10],[2,6],[8,9],[15,18]]) == 2
    assert sol.minMeetingRooms([[13,15],[1,13]]) == 1