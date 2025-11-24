# [ Name: Sort Colors ]  [ Category: two_pointers ]  [ Topic: two_pointers ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/sort-colors/ ]

"""
Given an array nums with n objects colored red (0), white (1), or blue (2), sort them in-place so that elements of the same color are adjacent and in the order red, white, and blue.
Do not return a new array, modify nums in-place.
Constraints: 1 <= nums.length <= 300, nums[i] is 0, 1, or 2.
Example: Input: nums = [2,0,2,1,1,0] Output: [0,0,1,1,2,2]
"""

from typing import List

def sortColors(nums: List[int]) -> None:
    pass

if __name__ == "__main__":
    arr = [2,0,2,1,1,0]; sortColors(arr); assert arr == [0,0,1,1,2,2]
    arr = [2,0,1]; sortColors(arr); assert arr == [0,1,2]
    arr = [0]; sortColors(arr); assert arr == [0]
    arr = [1]; sortColors(arr); assert arr == [1]
    arr = [2,2,2,2]; sortColors(arr); assert arr == [2,2,2,2]
    arr = [1,0,1,0,1,0]; sortColors(arr); assert arr == [0,0,0,1,1,1]
    arr = [0,1,2,1,0,2,1,0]; sortColors(arr); assert arr == [0,0,0,1,1,1,2,2]
    arr = [1,1,1]; sortColors(arr); assert arr == [1,1,1]
    arr = [2,1,2,0,2,1,0,1,0,2,1,0]; sortColors(arr); assert arr == [0,0,0,0,1,1,1,1,1,2,2,2]