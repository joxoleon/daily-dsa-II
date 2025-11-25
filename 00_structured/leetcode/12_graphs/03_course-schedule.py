# [ Name: Course Schedule ]  [ Category: graphs ]  [ Topic: graphs ]  [ Weight: 10 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/course-schedule/ ]

"""
Given the total number of courses and a list of prerequisite pairs, determine if it is possible to finish all courses. Each pair [a, b] means to take course a, you must first take course b.
Input: numCourses (int), prerequisites (List of [int, int] pairs)
Output: True if possible to finish all courses, otherwise False.
Constraints: 1 <= numCourses <= 2000, 0 <= prerequisites.length <= 5000
Example: numCourses = 2, prerequisites = [[1,0]] -> True
"""

from typing import List

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    pass

if __name__ == "__main__":
    assert canFinish(2, [[1,0]]) == True
    assert canFinish(2, [[1,0],[0,1]]) == False
    assert canFinish(3, [[1,0],[2,1]]) == True
    assert canFinish(3, [[1,0],[0,2],[2,1]]) == False
    assert canFinish(1, []) == True
    assert canFinish(5, []) == True
    assert canFinish(4, [[1,0],[2,1],[3,2]]) == True
    assert canFinish(4, [[1,0],[2,1],[0,2]]) == False