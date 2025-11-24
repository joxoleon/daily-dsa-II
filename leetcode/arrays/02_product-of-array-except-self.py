# [ Name: Product of Array Except Self ]  [ Category: arrays ]  [ Topic: arrays ]  [ Weight: 10 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/product-of-array-except-self/ ]

"""
Given an integer array nums of length n, return an array answer such that answer[i] is the product of all elements of nums except nums[i]. The solution must run in O(n) time without using division. 
1 <= nums.length <= 10^5
-30 <= nums[i] <= 30
Example: Input: nums = [1,2,3,4] Output: [24,12,8,6]
"""

from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    pass

if __name__ == "__main__":
    assert productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert productExceptSelf([0,1,2,3]) == [6,0,0,0]
    assert productExceptSelf([2,2,2,2]) == [8,8,8,8]
    assert productExceptSelf([5]) == [1]
    assert productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]
    assert productExceptSelf([4,3,2,1,2]) == [12,16,24,48,24]
    assert productExceptSelf([0,0]) == [0,0]
    assert productExceptSelf([10,2,5,0]) == [0,0,0,100]