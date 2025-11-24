# [ Name: First Missing Positive ]  [ Category: extra_20_must_know ]  [ Topic: extra_20_must_know ]  [ Weight: 10 ]  [ Difficulty: Hard ]
# [ Link: https://leetcode.com/problems/first-missing-positive/ ]

"""
Given an unsorted integer array nums, return the smallest missing positive integer.
The algorithm should run in O(n) time and use constant extra space.
Input: nums is a list of integers, may include negatives or zeros.
Output: an integer representing the first missing positive.
Constraints: 1 <= len(nums) <= 10^5; -2^31 <= nums[i] <= 2^31 - 1
Example: Input: nums = [3,4,-1,1] Output: 2
"""

from typing import List

def firstMissingPositive(nums: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert firstMissingPositive([1,2,0]) == 3
    assert firstMissingPositive([3,4,-1,1]) == 2
    assert firstMissingPositive([7,8,9,11,12]) == 1
    assert firstMissingPositive([1]) == 2
    assert firstMissingPositive([2]) == 1
    assert firstMissingPositive([-1,-2,-3]) == 1
    assert firstMissingPositive([1,2,3,4,5]) == 6
    assert firstMissingPositive([0,2,2,1,1]) == 3