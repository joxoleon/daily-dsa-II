# [ Name: Prefix Sum — Longest Subarray with Sum K ]  [ Category: arrays ]  [ Topic: prefix_sum_hashmap ]  [ Weight: 6 ]

"""
Problem Description:
Given a list of integers nums and an integer k, find the length of the longest contiguous subarray whose sum equals k.
Return 0 if no such subarray exists.

Constraints:
- 1 <= len(nums) <= 10^5
- -10^9 <= nums[i], k <= 10^9

Example:
Input: nums = [1, -1, 5, -2, 3], k = 3 -> Output: 4
"""

from typing import List

def longest_subarray_sum_k(nums: List[int], k: int) -> int:
    pass

if __name__ == "__main__":
    assert longest_subarray_sum_k([1, -1, 5, -2, 3], 3) == 4
    assert longest_subarray_sum_k([-2, -1, 2, 1], 1) == 2
    assert longest_subarray_sum_k([1, 2, 3], 3) == 1
    assert longest_subarray_sum_k([1, 2, 3], 6) == 3
    assert longest_subarray_sum_k([1, 2, 3], 7) == 0
    assert longest_subarray_sum_k([3], 3) == 1
    assert longest_subarray_sum_k([-1, -1, 1, 2], 1) == 3
    assert longest_subarray_sum_k([5, -1, 2, 3, -2, 4], 7) == 4

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
