# [ Name: Binary Search — Search in Rotated Sorted Array ]  [ Category: arrays ]  [ Topic: binary_search_rotated ]  [ Weight: 9 ]

"""
Problem Description:
Given a rotated sorted array of distinct integers and a target value, find the index of the target in the array.
If the target is not found, return -1.
The array may have been rotated at some unknown pivot.
You must design an algorithm with O(log n) runtime complexity.

Constraints:
- 1 <= len(nums) <= 10^4
- All elements are unique

Example:
Input: nums = [4,5,6,7,0,1,2], target = 0 -> Output: 4
"""

from typing import List

def search_rotated(nums: List[int], target: int) -> int:
    pass

if __name__ == "__main__":
    assert search_rotated([4,5,6,7,0,1,2], 0) == 4
    assert search_rotated([4,5,6,7,0,1,2], 3) == -1
    assert search_rotated([1], 1) == 0
    assert search_rotated([1], 0) == -1
    assert search_rotated([6,7,1,2,3,4,5], 4) == 5
    assert search_rotated([5,6,7,1,2,3,4], 7) == 2
    assert search_rotated([5,1,2,3,4], 1) == 1
    assert search_rotated([8,9,2,3,4], 8) == 0

    print("All tests passed.")
