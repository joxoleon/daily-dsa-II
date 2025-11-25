# [ Name: Prefix Sum — Count Subarrays with Even/Odd Sum ]  [ Category: arrays ]  [ Topic: prefix_sum_parity ]  [ Weight: 4 ]

"""
Problem Description:
Given a list of integers nums, count the number of contiguous subarrays whose sum is even.
Return that count as an integer.

Constraints:
- 1 <= len(nums) <= 10^5
- -10^9 <= nums[i] <= 10^9

Example:
Input: [1, 2, 3] -> Output: 2  (subarrays: [2], [1,2,3])
"""

from typing import List

def count_even_sum_subarrays(nums: List[int]) -> int:
    pass


if __name__ == "__main__":
    assert count_even_sum_subarrays([1, 2, 3]) == 2
    assert count_even_sum_subarrays([2, 4, 6]) == 6
    assert count_even_sum_subarrays([1, 1, 1, 1]) == 4
    assert count_even_sum_subarrays([1]) == 0
    assert count_even_sum_subarrays([0]) == 1
    assert count_even_sum_subarrays([1, 3, 5, 7, 9]) == 6
    assert count_even_sum_subarrays([-2, 2, -2, 2]) == 8
    assert count_even_sum_subarrays([]) == 0

    print("All tests passed.")
