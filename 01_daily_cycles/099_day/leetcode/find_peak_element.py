# [ Name: Find Peak Element ]  [ Category: binary_search ]  [ Topic: binary_search ]  [ Weight: 7 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/find-peak-element/ ]

"""
Given an array of integers nums, find an index of a peak element.
A peak element is an element that is strictly greater than its neighbors.
Return the index of any peak element.
You may assume that nums[i] != nums[i+1].
Constraints: 1 <= nums.length <= 1000, -2^31 <= nums[i] <= 2^31-1.
Example: Input: nums = [1,2,1,3,5,6,4] Output: 5
"""

from typing import List

def findPeakElement(nums: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert isinstance(findPeakElement([1,2,3,1]), int)
    assert isinstance(findPeakElement([1,2,1,3,5,6,4]), int)
    assert findPeakElement([1]) == 0
    assert findPeakElement([2,1]) in [0]
    assert findPeakElement([1,2]) in [1]
    assert findPeakElement([1,3,2,1]) in [1]
    assert findPeakElement([1,2,3,4,5]) == 4
    assert findPeakElement([5,4,3,2,1]) == 0