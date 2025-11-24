# [ Name: Search in Rotated Sorted Array ]  [ Category: binary_search ]  [ Topic: binary_search ]  [ Weight: 10 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/search-in-rotated-sorted-array/ ]

"""
Given an array of distinct integers nums sorted in ascending order, then rotated at an unknown pivot, and an integer target, return the index of target if it is in nums, or -1 otherwise.
Input: nums: List[int], target: int
Output: int (index of target, or -1)
Constraints: 1 <= nums.length <= 5000, -10^4 <= nums[i], target <= 10^4, nums contains distinct values.
Example: nums = [4,5,6,7,0,1,2], target = 0 => Output: 4
"""

from typing import List

def search(nums: List[int], target: int) -> int:
    pass

if __name__ == "__main__":
    assert search([4,5,6,7,0,1,2], 0) == 4
    assert search([4,5,6,7,0,1,2], 3) == -1
    assert search([1], 0) == -1
    assert search([1], 1) == 0
    assert search([5,1,3], 5) == 0
    assert search([5,1,3], 1) == 1
    assert search([5,1,3], 3) == 2
    assert search([6,7,8,9,1,2,3,4,5], 2) == 5