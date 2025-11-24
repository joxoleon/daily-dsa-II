# [ Name: Contains Duplicate ]  [ Category: arrays ]  [ Topic: arrays ]  [ Weight: 7 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/contains-duplicate/ ]

"""
Given an integer array nums, return true if any value appears at least twice in the array, and false if every element is distinct. Constraints: 1 <= nums.length <= 10^5; -10^9 <= nums[i] <= 10^9.
Example: Input: nums = [1,2,3,1] Output: true
"""

from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    pass

if __name__ == "__main__":
    assert containsDuplicate([1,2,3,1]) == True
    assert containsDuplicate([1,2,3,4]) == False
    assert containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True
    assert containsDuplicate([0]) == False
    assert containsDuplicate([99,100,101,102,103]) == False
    assert containsDuplicate([5,5,5,5,5]) == True
    assert containsDuplicate([-1,-2,-3,-4,-1]) == True
    assert containsDuplicate([4,3,2,1,0,-1,-2,-3,-4,-4]) == True