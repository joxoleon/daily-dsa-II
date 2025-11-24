# [ Name: Container With Most Water ]  [ Category: two_pointers ]  [ Topic: two_pointers ]  [ Weight: 10 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/container-with-most-water/ ]

"""
Given an integer array height where each element represents the height of a vertical line on the x-axis, find two lines that together with the x-axis form a container that holds the most water.
Return the maximum amount of water a container can store.
Constraints: 2 <= len(height) <= 10^5, 0 <= height[i] <= 10^4.
Example: height = [1,8,6,2,5,4,8,3,7] returns 49.
"""

from typing import List

def maxArea(height: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert maxArea([1,1]) == 1
    assert maxArea([4,3,2,1,4]) == 16
    assert maxArea([1,2,1]) == 2
    assert maxArea([2,3,10,5,7,8,9]) == 36
    assert maxArea([1,1000,1,1000,1]) == 3000
    assert maxArea([1,2,4,3]) == 4
    assert maxArea([6,4,3,1,4,6,99,62,1,2,4,5,3,2]) == 62