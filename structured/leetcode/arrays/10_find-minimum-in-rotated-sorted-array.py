# [ Name: Find Minimum in Rotated Sorted Array ]  [ Category: arrays ]  [ Topic: arrays ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/ ]

"""
Given a rotated sorted array of unique integers, return the minimum element.
Input: nums, a list of integers representing the rotated array.
Output: An integer, the smallest value in nums.
Constraints: 1 <= len(nums) <= 5000; nums has no duplicates.
Example: nums = [3,4,5,1,2] -> Output: 1
"""

from typing import List

def findMin(nums: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert findMin([3,4,5,1,2]) == 1
    assert findMin([4,5,6,7,0,1,2]) == 0
    assert findMin([11,13,15,17]) == 11
    assert findMin([2,3,4,5,6,7,8,1]) == 1
    assert findMin([1]) == 1
    assert findMin([2,1]) == 1
    assert findMin([5,1,2,3,4]) == 1
    assert findMin([1,2,3,4,5]) == 1
