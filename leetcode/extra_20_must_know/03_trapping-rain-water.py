# [ Name: Trapping Rain Water ]  [ Category: extra_20_must_know ]  [ Topic: extra_20_must_know ]  [ Weight: 10 ]  [ Difficulty: Hard ]
# [ Link: https://leetcode.com/problems/trapping-rain-water/ ]

"""
Given a list of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
Input: A list of integers 'height'.
Output: An integer representing total trapped water.
Constraints: 1 <= len(height) <= 2 * 10^4, 0 <= height[i] <= 10^5.
Example:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1], Output: 6
"""

from typing import List

def trap(height: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert trap([4,2,0,3,2,5]) == 9
    assert trap([1,0,1]) == 1
    assert trap([2,0,2]) == 2
    assert trap([3,0,1,0,2]) == 5
    assert trap([0,0,0,0]) == 0
    assert trap([5,4,1,2]) == 1
    assert trap([1,2,3,4,5]) == 0