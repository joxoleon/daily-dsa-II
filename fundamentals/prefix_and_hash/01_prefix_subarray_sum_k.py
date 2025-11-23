# [ Name: Prefix Sum — Subarray Sum Equals K ]  [ Category: arrays ]  [ Topic: prefix_sum_hashmap ]  [ Weight: 7 ]

"""
Problem Description:
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals k.
Return 0 if no such subarray exists.
The array may contain negative numbers and zeros.

Constraints:
- 1 <= len(nums) <= 2 * 10^4
- -1000 <= nums[i], k <= 100000

Example:
Input: nums = [1,2,3], k = 3  Output: 2
"""

from typing import List

def subarray_sum(nums: List[int], k: int) -> int:
    pass

if __name__ == "__main__":
    assert subarray_sum([1,2,3], 3) == 2
    assert subarray_sum([1,1,1], 2) == 2
    assert subarray_sum([1,-1,0], 0) == 3
    assert subarray_sum([3,4,7,2,-3,1,4,2], 7) == 4
    assert subarray_sum([1], 1) == 1
    assert subarray_sum([1], 0) == 0
    assert subarray_sum([-1,-1,1], 0) == 1
    assert subarray_sum([0,0,0,0], 0) == 10

    print("All tests passed.")
