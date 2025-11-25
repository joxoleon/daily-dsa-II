# [ Name: Binary Search — Rightmost Occurrence ]  [ Category: binary_search ]  [ Topic: binary_search_boundaries ]  [ Weight: 7 ]

"""
Problem Description:
Given a sorted list of integers nums and an integer target, return the index of the rightmost (last) occurrence of target in nums.
If target is not present, return -1.
Assume nums may contain duplicates and is sorted in non-decreasing order.
Constraints:
- 0 <= len(nums) <= 10^5
- -10^9 <= nums[i], target <= 10^9

Example:
Input: nums = [1,2,2,2,3], target = 2 -> Output: 3
"""

from typing import List

def search_right(nums: List[int], target: int) -> int:
    pass

if __name__ == "__main__":
    assert search_right([1,2,2,2,3], 2) == 3
    assert search_right([1,1,1,1], 1) == 3
    assert search_right([1,2,3,4,5], 3) == 2
    assert search_right([1,2,3,4,5], 6) == -1
    assert search_right([], 1) == -1
    assert search_right([1,2,3], 0) == -1
    assert search_right([2,2,2,2,2], 2) == 4
    assert search_right([1,3,3,5,5,5,7], 5) == 5

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
