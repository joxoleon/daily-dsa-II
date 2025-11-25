# [ Name: DP — Longest Increasing Subsequence (O(n^2)) ]  [ Category: dp ]  [ Topic: 1d_dp ]  [ Weight: 7 ]

"""
Problem Description:
Given a list of integers nums, find the length of the longest strictly increasing subsequence.
A subsequence is a sequence derived from nums by removing zero or more elements without changing the order.
Return the length as an integer.

Constraints:
- 1 <= len(nums) <= 2500
- -10^4 <= nums[i] <= 10^4

Example:
Input: [10, 9, 2, 5, 3, 7, 101, 18] -> Output: 4
"""

from typing import List

def length_of_lis(nums: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4
    assert length_of_lis([7, 7, 7, 7]) == 1
    assert length_of_lis([1]) == 1
    assert length_of_lis([1, 2, 3, 4, 5]) == 5
    assert length_of_lis([5, 4, 3, 2, 1]) == 1
    assert length_of_lis([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6
    assert length_of_lis([2, 2]) == 1

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
