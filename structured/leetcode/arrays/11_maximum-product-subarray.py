# [ Name: Maximum Product Subarray ]  [ Category: arrays ]  [ Topic: arrays ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/maximum-product-subarray/ ]

"""
Given an integer array nums, find the contiguous subarray within nums that has the largest product and return its product.
Input: A list of integers nums where 1 <= nums.length <= 2 * 10^4 and -10 <= nums[i] <= 10.
Output: An integer representing the maximum product of any contiguous subarray.
Constraints: The input contains at least one integer. The product subarray may be of length 1.
Example: Input: nums = [2,3,-2,4]  Output: 6 (subarray [2,3])
"""

from typing import List

def maxProduct(nums: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert maxProduct([2,3,-2,4]) == 6
    assert maxProduct([-2,0,-1]) == 0
    assert maxProduct([0,2]) == 2
    assert maxProduct([-2,3,-4]) == 24
    assert maxProduct([-1,-3,-10,0,60]) == 60
    assert maxProduct([-2,-3,0,-2,-40]) == 80
    assert maxProduct([6,-3,-10,0,2]) == 180
    assert maxProduct([2,-5,-2,-4,3]) == 24