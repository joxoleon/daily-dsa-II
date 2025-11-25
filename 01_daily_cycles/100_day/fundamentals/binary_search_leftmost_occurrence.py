# [ Name: Binary Search — Leftmost Occurrence ]  [ Category: binary_search ]  [ Topic: binary_search_boundaries ]  [ Weight: 7 ]

"""
Problem Description:
Given a sorted list of integers nums and an integer target, return the index of the leftmost occurrence of target in nums.
If target is not present, return -1.
nums may contain duplicates.
Constraints:
- 0 <= len(nums) <= 10^5
- All elements are integers in the range [-10^9, 10^9]

Example:
Input: nums = [1, 2, 2, 2, 3], target = 2 -> Output: 1
"""

from typing import List

def search_left(nums: List[int], target: int) -> int:
    pass

if __name__ == "__main__":
    assert search_left([1, 2, 2, 2, 3], 2) == 1
    assert search_left([1, 1, 1, 1, 2], 1) == 0
    assert search_left([2, 3, 4, 5], 1) == -1
    assert search_left([], 10) == -1
    assert search_left([5], 5) == 0
    assert search_left([4, 4, 4, 4], 4) == 0
    assert search_left([1, 3, 3, 3, 5, 7], 3) == 1
    assert search_left([0, 1, 2, 3, 4], 4) == 4

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
