# [ Name: Two Pointers — Two Sum in Sorted Array ]  [ Category: arrays ]  [ Topic: two_pointers ]  [ Weight: 9 ]

"""
Problem Description:
Given a sorted array of integers and an integer target, determine if there exist two numbers in the array that sum up to the target.
Return True if such a pair exists, otherwise return False.

Constraints:
- Input: sorted list of integers (may be empty), target integer
- Each input has at most one valid pair; numbers may be negative
- Length of array: 0 <= len(nums) <= 10^5

Example:
Input: nums = [1, 2, 4, 7, 11], target = 15 -> Output: True
"""

from typing import List

def two_sum_sorted(nums: List[int], target: int) -> bool:
    pass

if __name__ == "__main__":
    assert two_sum_sorted([1, 2, 4, 7, 11], 15) == True
    assert two_sum_sorted([-5, -1, 0, 3, 9], 8) == True
    assert two_sum_sorted([3, 5, 8, 12], 7) == False
    assert two_sum_sorted([], 5) == False
    assert two_sum_sorted([2], 4) == False
    assert two_sum_sorted([1, 2, 3, 4], 10) == False
    assert two_sum_sorted([1, 1, 3, 5], 2) == True
    assert two_sum_sorted([0, 1, 2, 3, 9], 9) == True

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
