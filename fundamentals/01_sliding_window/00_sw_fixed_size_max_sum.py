# [ Name: Sliding Window — Max Sum of Fixed Window ]  [ Category: arrays ]  [ Topic: sliding_window_fixed ]  [ Weight: 6 ]

"""
Problem Description:
Given a list of integers `nums` and an integer `k`, find the maximum sum of any contiguous subarray of length `k`.
Return the maximum sum as an integer.

Constraints:
- 1 <= len(nums) <= 10^5
- 1 <= k <= len(nums)
- -10^4 <= nums[i] <= 10^4

Example:
Input: nums = [2, 1, 5, 1, 3, 2], k = 3 -> Output: 9
"""

from typing import List

def max_sum_fixed(nums: List[int], k: int) -> int:
    pass

if __name__ == "__main__":
    assert max_sum_fixed([2, 1, 5, 1, 3, 2], 3) == 9
    assert max_sum_fixed([1, 2, 3, 4, 5], 2) == 9
    assert max_sum_fixed([5, 4, -1, 7, 8], 1) == 8
    assert max_sum_fixed([-2, -1, -3, -4], 2) == -3
    assert max_sum_fixed([3, 3, 3, 3, 3], 5) == 15
    assert max_sum_fixed([10], 1) == 10
    assert max_sum_fixed([1, 2, 3, 100, 2, 4], 2) == 102
    assert max_sum_fixed([5, -2, 3, -1, 2, 6, -3], 4) == 10

    print("All tests passed.")
