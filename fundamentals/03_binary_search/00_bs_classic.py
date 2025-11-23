# [ Name: Binary Search — Classic Index Search ]  [ Category: arrays ]  [ Topic: binary_search ]  [ Weight: 8 ]

"""
Problem Description:
Given a sorted list of integers in ascending order, return the index of a given target value.
If the target is not found, return -1.
Assume no duplicate elements exist in the list.

Constraints:
- Input: nums (0 <= len(nums) <= 10^5), target (int)
- All elements are unique.

Example:
Input: nums = [1,3,5,7,9], target = 5 -> Output: 2
"""

from typing import List

def binary_search(nums: List[int], target: int) -> int:
    pass

if __name__ == "__main__":
    assert binary_search([1,3,5,7,9], 5) == 2
    assert binary_search([1,3,5,7,9], 1) == 0
    assert binary_search([1,3,5,7,9], 9) == 4
    assert binary_search([1,3,5,7,9], 10) == -1
    assert binary_search([5], 5) == 0
    assert binary_search([5], 0) == -1
    assert binary_search([], 7) == -1
    assert binary_search([2,4,6,8,10,12], 8) == 3

    print("All tests passed.")
