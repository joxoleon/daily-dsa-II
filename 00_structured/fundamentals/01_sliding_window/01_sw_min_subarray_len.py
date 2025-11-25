# [ Name: Sliding Window — Minimum Subarray Length ]  [ Category: arrays ]  [ Topic: sliding_window_variable ]  [ Weight: 7 ]

"""
Problem Description:
Given an array of positive integers nums and a positive integer target, find the minimal length of a contiguous subarray of which the sum is at least target. Return 0 if there is no such subarray.

Constraints:
- 1 <= len(nums) <= 10^5
- 1 <= nums[i] <= 10^4
- 1 <= target <= 10^9

Example:
Input: target = 7, nums = [2,3,1,2,4,3] -> Output: 2
"""


from typing import List

def min_subarray_len(target: int, nums: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert min_subarray_len(7, [2,3,1,2,4,3]) == 2
    assert min_subarray_len(15, [1,2,3,4,5]) == 5
    assert min_subarray_len(11, [1,2,3,4,5]) == 3
    assert min_subarray_len(4, [1,4,4]) == 1
    assert min_subarray_len(100, [1,2,3,4,5]) == 0
    assert min_subarray_len(5, [5,1,1,1,1]) == 1
    assert min_subarray_len(8, [2,3,1,2,3,7]) == 1
    assert min_subarray_len(6, [1,1,1,1,1,6]) == 1

    print("All tests passed.")
