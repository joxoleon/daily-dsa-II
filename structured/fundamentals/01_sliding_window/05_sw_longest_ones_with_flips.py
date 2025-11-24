# [ Name: Sliding Window — Longest Ones After Flips ]  [ Category: arrays ]  [ Topic: sliding_window_zero_flips ]  [ Weight: 7 ]

"""
Problem Description:
Given a binary array nums and an integer k, return the length of the longest subarray containing only 1's after flipping at most k 0's to 1's.
If no flips are allowed, return the longest stretch of consecutive 1's.
Constraints:
- 1 <= len(nums) <= 10^5
- 0 <= k <= len(nums)
Example:
Input: nums = [1,1,0,0,1,1,1,0], k = 2 -> Output: 7
"""

from typing import List

def longest_ones(nums: List[int], k: int) -> int:
    pass

if __name__ == "__main__":
    assert longest_ones([1,1,0,0,1,1,1,0], 2) == 7
    assert longest_ones([0,0,0,1], 4) == 4
    assert longest_ones([1,0,1,0,1,0], 1) == 3
    assert longest_ones([1,1,1,1], 0) == 4
    assert longest_ones([0,0,0], 0) == 0
    assert longest_ones([0,1,0,1,0,1,0], 3) == 7
    assert longest_ones([1,0,1,1,0,1,1,1,0], 2) == 8
    assert longest_ones([1], 0) == 1

    print("All tests passed.")
