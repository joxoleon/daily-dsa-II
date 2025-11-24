# [ Name: Maximum Subarray ]  [ Category: arrays ]  [ Topic: arrays ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/maximum-subarray/ ]

"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Input: nums (List[int]), output: int (maximum subarray sum).
Constraints: 1 <= nums.length <= 10^5; -10^4 <= nums[i] <= 10^4.
Example: nums = [-2,1,-3,4,-1,2,1,-5,4] => Output: 6 (subarray [4,-1,2,1])
"""

from typing import List

def maxSubArray(nums: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert maxSubArray([1]) == 1
    assert maxSubArray([5,4,-1,7,8]) == 23
    assert maxSubArray([-1]) == -1
    assert maxSubArray([-2,-1]) == -1
    assert maxSubArray([0,0,0,0]) == 0
    assert maxSubArray([-1,0,-2]) == 0
    assert maxSubArray([1,2,3,4]) == 10