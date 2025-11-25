# [ Name: Course Schedule II ]  [ Category: graphs ]  [ Topic: graphs ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/course-schedule-ii/ ]

"""
Given the total number of courses and a list of prerequisite pairs, return the order in which you can finish all courses. If it is impossible, return an empty list. There are n courses labeled from 0 to n - 1. Each prerequisite pair is formatted as [a, b], indicating you must take b before a. Constraints: 1 <= numCourses <= 2000, prerequisites length <= 5000. Example: Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]], Output: [0,2,1,3] or [0,1,2,3].
"""

from typing import List

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    pass

if __name__ == "__main__":
    assert findOrder(2, [[1,0]]) in ([0,1], [1,0])
    assert findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) in ([0,2,1,3],[0,1,2,3])
    assert findOrder(1, []) == [0]
    assert findOrder(2, [[0,1],[1,0]]) == []
    assert findOrder(3, [[1,0],[1,2],[0,1]]) == []
    assert findOrder(3, []) in ([0,1,2], [0,2,1], [1,0,2], [1,2,0], [2,0,1], [2,1,0])
    assert findOrder(5, [[1,4],[2,4],[3,1],[3,2]]) in ([0,4,1,2,3],[4,1,2,3,0],[4,2,1,3,0],[4,0,1,2,3],[4,0,2,1,3])
    assert findOrder(2, []) in ([0,1], [1,0])
