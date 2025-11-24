# [ Name: Largest Rectangle in Histogram ]  [ Category: stack ]  [ Topic: stack ]  [ Weight: 10 ]  [ Difficulty: Hard ]
# [ Link: https://leetcode.com/problems/largest-rectangle-in-histogram/ ]

"""
Given an integer array heights representing the heights of bars in a histogram, find the area of the largest rectangle that can be formed from contiguous bars.
Input: A list of integers heights of length n.
Output: An integer representing the maximal rectangular area.
Constraints: 1 <= heights.length <= 10^5, 0 <= heights[i] <= 10^4.
Example: Input: heights = [2,1,5,6,2,3]; Output: 10
"""

from typing import List

def largestRectangleArea(heights: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert largestRectangleArea([2,1,5,6,2,3]) == 10
    assert largestRectangleArea([2,4]) == 4
    assert largestRectangleArea([1,1,1,1]) == 4
    assert largestRectangleArea([4,2,0,3,2,5]) == 6
    assert largestRectangleArea([6,7,5,2,4,5,9,3]) == 16
    assert largestRectangleArea([0,9]) == 9
    assert largestRectangleArea([1]) == 1
    assert largestRectangleArea([10000]*100000) == 1000000000