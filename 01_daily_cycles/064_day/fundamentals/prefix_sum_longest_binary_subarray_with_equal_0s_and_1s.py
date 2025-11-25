# [ Name: Prefix Sum — Longest Binary Subarray with Equal 0s and 1s ]  [ Category: arrays ]  [ Topic: prefix_sum_hashmap ]  [ Weight: 8 ]

"""
Problem Description:
Given a binary array nums (containing only 0s and 1s), find the length of the longest contiguous subarray with an equal number of 0s and 1s.
Return the length of this subarray. If there is none, return 0.

Constraints:
- 1 <= len(nums) <= 10^5
- Each element of nums is either 0 or 1.

Example:
Input: [0,1,0] -> Output: 2
"""

from typing import List

def find_max_length(nums: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert find_max_length([0,1,0]) == 2
    assert find_max_length([0,1,1,0,1,1,0,0]) == 8
    assert find_max_length([0,0,1,1,0]) == 4
    assert find_max_length([1,1,1,1]) == 0
    assert find_max_length([0,0,0,1,1,1,0]) == 6
    assert find_max_length([0,1]) == 2
    assert find_max_length([0]) == 0
    assert find_max_length([1,0,1,1,1,0,0]) == 6

    print("All tests passed.")
